import logging

from db.db_interface import DBInterface

logger = logging.getLogger(__name__)


class Device(DBInterface):
    def __init__(self):
        super(Device, self).__init__("device")
