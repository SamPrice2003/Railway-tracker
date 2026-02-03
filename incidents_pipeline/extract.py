"Script which extracts incident feed data from the National Rail API."

from os import environ as ENV, _Environ
from time import sleep
from logging import getLogger, basicConfig, INFO
from json import dumps, loads
from re import sub

from xmltodict import parse
from dotenv import load_dotenv
from stomp import Connection12, ConnectionListener
from stomp.utils import Frame

logger = getLogger(__name__)
basicConfig(level=INFO)


class Listener(ConnectionListener):

    def __init__(self):
        self.messages = []

    def get_clean_message_dict(self, msg: str) -> str:
        """Cleans message contents according to discrepancies noted on API.
        Returns a corresponding dictionary."""

        msg = msg.replace(
            "uk.co.nationalrail.xml.incident.PtIncidentStructure", "PtIncident")

        return loads(sub(r"\/?ns[23]:", "", msg))

    def on_message(self, msg: Frame):
        """Whenever we receive a message, parse it as a dict and clean the key names."""
        try:
            logger.info("Message received.")

            data = self.get_clean_message_dict(dumps(parse(msg.body)))
            data = data["PtIncident"]

            self.messages.append(data)

        except Exception as e:
            logger.error(str(e))

    def pop_message(self) -> dict:
        """Removes and returns the message first in the list of messages.
        Returns None if list is empty."""

        if len(self.messages) != 0:
            return self.messages.pop(0)

        return None


def get_stomp_connection(config: _Environ) -> Connection12:
    """Returns a STOMP connection to the National Rail Real Time Incidents API."""

    return Connection12(
        host_and_ports=[(config["STOMP_HOST"], config["STOMP_PORT"])],
        auto_decode=False)


def connect_and_subscribe(config: _Environ, listener: Listener, conn: Connection12) -> None:
    """Subscribes the connection to the National Rail Real Time Incidents topic.
    Requires a STOMP listener and a connection."""

    conn.set_listener("", listener)

    conn.connect(username=config["STOMP_USERNAME"],
                 passcode=config["STOMP_PASSWORD"],
                 wait=True)

    conn.subscribe(destination=f"/topic/{config["STOMP_TOPIC"]}",
                   id="1",
                   ack="auto")


def get_stomp_listener(config: _Environ) -> Listener:
    """Returns a STOMP listener that is connected and subscribed
    to National Rail Real Time Incidents Feed."""

    conn = get_stomp_connection(config)

    listener = Listener()

    connect_and_subscribe(config, listener, conn)

    return listener


if __name__ == "__main__":

    load_dotenv()

    listener = get_stomp_listener(ENV)

    while True:
        message = listener.pop_message()

        if message:
            print(message)

        sleep(1)
