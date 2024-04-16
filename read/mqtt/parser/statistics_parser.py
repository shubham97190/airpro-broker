import logging

from db.db_client_factory import DBClientFactory, db_client_factory
from protobuf.aircnms_stats_pb2 import Report
from read.mqtt.dto.client_dto import StatisticsDto
from read.mqtt.parser.interface import ParserInterface

logger = logging.getLogger(__name__)


class StatisticsParser(ParserInterface):

    def __init__(self):
        super(StatisticsParser, self).__init__(Report())
        self.creators = db_client_factory.get_all_creators()

    def deserialize(self, payload):
        logger.info("Statistics Parser initiated for payload %s", payload)
        message_to_dict = super(StatisticsParser, self).extract_data(payload)

        if message_to_dict:
            serial_num = message_to_dict['serialNum']
            device_id = message_to_dict['deviceId']
            mac_addr = message_to_dict['macAddr']
            logger.info("Data Received for serialNum [%s] Device Id [%s] mac_addr [%s]", serial_num, device_id,
                        mac_addr)

            for key in self.creators:
                try:
                    data_to_push = message_to_dict[key]
                    logger.info("is Data Available for key %s data %s", key, data_to_push)
                    if data_to_push:
                        data = StatisticsDto(serial_num, device_id, mac_addr, data_to_push)
                        var = db_client_factory.get_db_client(key).create(self, data)
                        logger.info("Response %s ", var)
                except Exception as error:
                    logger.error("No key found %s ", key)
                    logger.error("An exception occurred:", type(error).__name__, "–", error)

    def serialize(self):
        pass
