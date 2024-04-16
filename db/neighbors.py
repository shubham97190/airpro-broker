import logging

from db.db_interface import DBInterface

logger = logging.getLogger(__name__)


class Neighbor(DBInterface):
    def __init__(self):
        super(Neighbor, self).__init__("neighbors")

