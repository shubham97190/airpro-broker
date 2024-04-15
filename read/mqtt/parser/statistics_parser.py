import logging

from protobuf.aircnms_stats_pb2 import Report
from read.mqtt.dto.client_dto import StatisticsDto
from read.mqtt.parser.interface import ParserInterface
from db.client import Client
logger = logging.getLogger(__name__)


class StatisticsParser(ParserInterface):

    def __init__(self):
        super(StatisticsParser, self).__init__(Report())

    def deserialize(self, payload):
        logger.info("Statistics Parser initiated for payload %s", payload)
        message_to_dict = super(StatisticsParser, self).extract_data(payload)
        if message_to_dict:
            client = Client()
            logger.info("Statistics serialNum  %s", message_to_dict['serialNum'])
            logger.info("Statistics device_id  %s", message_to_dict['deviceId'])
            logger.info("Statistics mac_addr %s", message_to_dict['macAddr'])
            
            if 'clients' in message_to_dict:
                client_data = StatisticsDto(message_to_dict['serialNum'], message_to_dict['deviceId'], message_to_dict['macAddr'], message_to_dict['clients'])
                logger.info("Statistics clients data  %s", client_data)
                # client.connected_client.create_client(client_data)
            
            device_data = StatisticsDto(message_to_dict['serialNum'], message_to_dict['deviceId'], message_to_dict['macAddr'], message_to_dict['device'])
            logger.info("Statistics device data  %s", device_data)
            # client.device.create_device(device_data)
            
            vif_data = StatisticsDto(message_to_dict['serialNum'], message_to_dict['deviceId'], message_to_dict['macAddr'], message_to_dict['vif'])
            logger.info("Statistics vif data  %s", vif_data)
            # client.vif.create_vif(vif_data)
            
            neighbors_data = StatisticsDto(message_to_dict['serialNum'], message_to_dict['deviceId'], message_to_dict['macAddr'], message_to_dict['neighbors'])
            logger.info("Statistics neighbors data  %s", neighbors_data)
            # client.neighbor.create_neighbor(neighbors_data)
            
            
    def serialize(self):
        pass
