import logging

from db.db_interface import DBInterface

logger = logging.getLogger(__name__)


class VIF(DBInterface):
    def __init__(self):
        super(VIF, self).__init__("vif")
