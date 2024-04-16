import logging

from db.db_interface import DBInterface

logger = logging.getLogger(__name__)


class BaseDevice(DBInterface):
    def __init__(self):
        super(BaseDevice, self).__init__("base-device")
