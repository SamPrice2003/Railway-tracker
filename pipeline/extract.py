"Script which extracts data from the National Rail API."

from os import environ as ENV, _Environ
from socket import getfqdn
from time import sleep
import logging
from io import BytesIO
from zlib import decompress, MAX_WBITS

from dotenv import load_dotenv
from stomp import Connection12, ConnectionListener

CLIENT_ID = getfqdn()
HEARTBEAT_INTERVAL_MS = 15000
RECONNECT_DELAY_SECS = 15

logging.basicConfig(level=logging.INFO)

try:
    import PPv16
except ModuleNotFoundError:
    logging.error(
        "Class files not found - please configure the client following steps in README.md!")


class StompClient(ConnectionListener):

    def on_heartbeat(self):
        logging.info('Received a heartbeat')

    def on_heartbeat_timeout(self):
        logging.error('Heartbeat timeout')

    def on_error(self, message):
        logging.error(message)

    def on_disconnected(self):
        logging.warning(
            'Disconnected - waiting %s seconds before exiting' % RECONNECT_DELAY_SECS)
        sleep(RECONNECT_DELAY_SECS)
        exit(-1)

    def on_connecting(self, host_and_port):
        logging.info('Connecting to ' + host_and_port[0])

    def on_message(self, frame):
        try:
            logging.info('Message sequence=%s, type=%s received', frame.headers['SequenceNumber'],
                         frame.headers['MessageType'])
            bio = BytesIO()
            bio.write(str.encode('utf-16'))
            bio.seek(0)
            msg = decompress(frame.body, MAX_WBITS | 32)
            logging.debug(msg)
            obj = PPv16.CreateFromDocument(msg)
            logging.info(
                "Successfully received a Darwin Push Port message from %s", obj.ts)
            logging.debug('Raw XML=%s' % msg)

        except Exception as e:
            logging.error(str(e))


def get_stomp_connection(config: _Environ) -> Connection12:
    """Returns a STOMP connection to the National Rail Darwin."""

    return Connection12(
        host_and_ports=[(config["DARWIN_HOST"], config["DARWIN_PORT"])],
        auto_decode=False,
        heartbeats=(HEARTBEAT_INTERVAL_MS, HEARTBEAT_INTERVAL_MS))


def subscribe_connection(config: _Environ, conn: Connection12) -> None:
    """Subscribes the connection to the the National Rail Darwin topic."""

    conn.set_listener("", StompClient())

    connect_header = {'client-id': config["DARWIN_USERNAME"] + '-' + CLIENT_ID}
    subscribe_header = {'activemq.subscriptionName': CLIENT_ID}

    conn.connect(username=config["DARWIN_USERNAME"],
                 passcode=config["DARWIN_PASSWORD"],
                 wait=True,
                 headers=connect_header)

    conn.subscribe(destination=f"/topic/{config["DARWIN_TOPIC"]}",
                   id='1',
                   ack='auto',
                   headers=subscribe_header)


if __name__ == "__main__":

    load_dotenv()

    conn = get_stomp_connection(ENV)

    subscribe_connection(ENV, conn)

    while True:
        sleep(1)
