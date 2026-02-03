"Script which extracts incident feed data from the National Rail API."

from os import environ as ENV, _Environ
from socket import getfqdn
from time import sleep
from logging import getLogger, basicConfig, INFO
from json import dumps, dump, loads
from re import sub

from xmltodict import parse
from dotenv import load_dotenv
from stomp import Connection12, ConnectionListener
from stomp.utils import Frame

CLIENT_ID = getfqdn()

logger = getLogger(__name__)
basicConfig(level=INFO)


class Listener(ConnectionListener):

    def get_clean_message_dict(self, msg: str) -> str:
        """Cleans message contents according to discrepancies noted on API.
        Returns a corresponding dictionary."""

        msg = msg.replace(
            "uk.co.nationalrail.xml.incident.PtIncidentStructure", "PtIncident")

        return loads(sub(r"\/?ns[23]:", "", msg))

    def extract_message_details(self, msg: str) -> dict:
        pass

    def on_message(self, msg: Frame):
        """Whenever we receive a message, parse it as a dict and clean the key names."""
        try:
            print(msg.headers)

            data = self.get_clean_message_dict(dumps(parse(msg.body)))

            with open("data.json", "w") as f:
                dump(data, f, indent=4)

        except Exception as e:
            logger.error(str(e))


def get_stomp_connection(config: _Environ) -> Connection12:
    """Returns a STOMP connection to the National Rail Real Time Incidents API."""

    return Connection12(
        host_and_ports=[(config["STOMP_HOST"], config["STOMP_PORT"])],
        auto_decode=False)


def connect_and_subscribe(config: _Environ, conn: Connection12) -> None:
    """Subscribes the connection to the National Rail Real Time Incidents topic."""

    conn.set_listener("", Listener())

    conn.connect(username=config["STOMP_USERNAME"],
                 passcode=config["STOMP_PASSWORD"],
                 wait=True)

    conn.subscribe(destination=f"/topic/{config["STOMP_TOPIC"]}",
                   id="1",
                   ack="auto")


if __name__ == "__main__":

    load_dotenv()

    conn = get_stomp_connection(ENV)

    connect_and_subscribe(ENV, conn)

    while True:
        sleep(1)
