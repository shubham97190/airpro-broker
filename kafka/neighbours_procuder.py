import logging

from constant.constant import KAFKA_TOPIC_NEIGHBOURS
from kafka.kafka_producer import AppKafkaProducer

logger = logging.getLogger(__name__)


class NeighboursProducer(AppKafkaProducer):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(NeighboursProducer, cls).__new__(cls)
            super().__init__(cls._instance, KAFKA_TOPIC_NEIGHBOURS)
            logger.info("[%s] Producer created...", KAFKA_TOPIC_NEIGHBOURS)
        return cls._instance
