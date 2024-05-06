import gzip
import json
import logging
import time
import zlib

from db.db_client_factory import db_client_factory
from kafka.kafka_producer import AppKafkaProducer
from kafka.kafka_publisher_factory import kf_client_factory
from read.mqtt.parser.interface import ParserInterface

logger = logging.getLogger(__name__)


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


class StatisticsParser(ParserInterface):

    def serialize(self):
        pass

    def __init__(self):
        super(StatisticsParser, self).__init__()
        self.creators = kf_client_factory.get_all_creators()

    # def deserialize(self, payload, kf_topic):
    #     try:
    #         start = time.time()
    #         # json_message = gzip.decompress(payload)
    #         json_data = json.loads(payload)
    #         logger.info("Statistics Parser initiated for payload %s", payload)
    #         if json_data:
    #             serial_num = json_data['serialNum']
    #             device_id = json_data['deviceId']
    #             mac_addr = json_data['macAddr']
    #             logger.info("Data Received for serialNum [%s] Device Id [%s] mac_addr [%s]", serial_num, device_id,
    #                         mac_addr)
    #             headers = [('device_id', device_id), ("mac_addr", mac_addr)]
    #             kf_client_factory.get_publisher_client(kf_topic).send_message(payload, headers)
    #             logger.info(u'Time take to push to Kafka: {}'.format((time.time() - start)))
    #             logger.info("Message sent %s", payload)
    #     except Exception as error:
    #         logger.error("An exception occurred:", type(error).__name__, "–", error)

    def deserialize(self, payload, kf_topic):
        try:
            start = time.time()
            logger.info("Statistics Parser initiated for payload %s", payload)
            if payload:
                headers = []
                kf_client_factory.get_publisher(kf_topic).send_message(payload, headers)
                logger.info(u'Message sent, time take to push to Kafka: %s milliseconds', (time.time() - start) * 1000)
        except Exception as error:
            logger.error("An exception occurred:", type(error).__name__, "–", error)
