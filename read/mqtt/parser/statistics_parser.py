import logging

from protobuf.aircnms_stats_pb2 import Report
from read.mqtt.parser.interface import ParserInterface

logger = logging.getLogger(__name__)


class StatisticsParser(ParserInterface):

    def __init__(self):
        super(StatisticsParser, self).__init__(Report())

    def deserialize(self, payload):
        logger.info("Statistics Parser initiated for payload %s", payload)
        message_to_dict = super(StatisticsParser, self).extract_data(payload)
        if message_to_dict:
            logger.info("Statistics serialNum  %s", message_to_dict.serial_num)
            logger.info("Statistics device_id  %s", message_to_dict.device_id)
            logger.info("Statistics mac_addr %s", message_to_dict.mac_addr)
            logger.info("Statistics clients data  %s", message_to_dict.clients)
            logger.info("Statistics device data  %s", message_to_dict.device)
            logger.info("Statistics vif data  %s", message_to_dict.vif)
            logger.info("Statistics neighbors data  %s", message_to_dict.neighbors)

    def serialize(self):
        pass
