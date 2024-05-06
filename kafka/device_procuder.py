import logging

from cachetools.func import lru_cache

from constant.constant import KAFKA_TOPIC_DEVICE
from kafka.kafka_producer import AppKafkaProducer

logger = logging.getLogger(__name__)


class DeviceProducer(AppKafkaProducer):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(DeviceProducer, cls).__new__(cls)
            super(DeviceProducer, cls._instance).__init__(KAFKA_TOPIC_DEVICE)
            logger.info("[%s] Producer created...", KAFKA_TOPIC_DEVICE)
        return cls._instance
