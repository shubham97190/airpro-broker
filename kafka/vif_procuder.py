import logging

from constant.constant import KAFKA_TOPIC_VIF
from kafka.kafka_producer import AppKafkaProducer

logger = logging.getLogger(__name__)


class VIFProducer(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logger.info('Creating the object')
            cls._instance = super(VIFProducer, cls).__new__(cls)
            cls._instance.producer = AppKafkaProducer(KAFKA_TOPIC_VIF)
            logger.info("[%s] Producer created...", KAFKA_TOPIC_VIF)
        return cls._instance
