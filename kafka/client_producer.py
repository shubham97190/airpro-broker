import logging

from constant.constant import KAFKA_TOPIC_CLIENTS
from kafka.kafka_producer import AppKafkaProducer

logger = logging.getLogger(__name__)


class ClientProducer(AppKafkaProducer):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(ClientProducer, cls).__new__(cls)
            super().__init__(cls._instance, KAFKA_TOPIC_CLIENTS)
            logger.info("[%s] Producer created...", KAFKA_TOPIC_CLIENTS)
        return cls._instance
