"Script which extracts incident feed data from the National Rail API."

from os import environ as ENV, _Environ
from socket import getfqdn
from time import sleep
from logging import getLogger, basicConfig, INFO
from zlib import decompress, MAX_WBITS

from dotenv import load_dotenv
from stomp import Connection12, ConnectionListener
from stomp.utils import Frame

CLIENT_ID = getfqdn()

logger = getLogger(__name__)
basicConfig(level=INFO)


class Listener(ConnectionListener):

    def get_raw_message_body(self, msg: Frame) -> str:
        """Returns the raw contents of the message."""
        msg = decompress(msg.body, MAX_WBITS | 32)
        return msg

    def extract_message_details(self, msg: str) -> dict:
        pass

    def on_message(self, msg: Frame):
        """Whenever we receive a message."""
        try:
            print(msg.headers)
            data = self.get_raw_message_body(msg)
        except Exception as e:
            logger.error(str(e), type(e))


def get_stomp_connection(config: _Environ) -> Connection12:
    """Returns a STOMP connection to the National Rail Darwin."""

    return Connection12(
        host_and_ports=[(config["STOMP_HOST"], config["STOMP_PORT"])],
        auto_decode=False)


def subscribe_connection(config: _Environ, conn: Connection12) -> None:
    """Subscribes the connection to the the National Rail Darwin topic."""

    conn.set_listener("", Listener())

    connect_header = {'client-id': config["STOMP_USERNAME"] + '-' + CLIENT_ID}
    subscribe_header = {'activemq.subscriptionName': CLIENT_ID}

    conn.connect(username=config["STOMP_USERNAME"],
                 passcode=config["STOMP_PASSWORD"],
                 wait=True,
                 headers=connect_header)

    conn.subscribe(destination=f"/topic/{config["STOMP_TOPIC"]}",
                   id='1',
                   ack='auto',
                   headers=subscribe_header)


if __name__ == "__main__":

    load_dotenv()

    conn = get_stomp_connection(ENV)

    subscribe_connection(ENV, conn)

    while True:
        sleep(1)
