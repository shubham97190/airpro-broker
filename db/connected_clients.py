import logging

from db.db_interface import DBInterface

logger = logging.getLogger(__name__)


class ConnectedClient(DBInterface):
    def __init__(self):
        super(ConnectedClient, self).__init__("client")
