import json
import logging
import logging.config
import os.path
from os.path import exists

from dotenv import load_dotenv

from constant import constant
from constant.constant import KAFKA_TOPIC_DEVICE, MQTT_TOPIC_RECEIVER_DEVICE, KAFKA_TOPIC_NEIGHBOURS, \
    MQTT_TOPIC_RECEIVER_NEIGHBOURS, MQTT_TOPIC_RECEIVER_VIF, KAFKA_TOPIC_VIF, KAFKA_TOPIC_CLIENTS
from read.mqtt.client.app_broker_client import AppBrokerClient
from read.mqtt.dto.client_dto import SubsDto

logger = logging.getLogger(__name__)


def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    load_dotenv()
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == '__main__':
    setup_logging()
    # f1 = AppBrokerClient(SubsDto(MQTT_TOPIC_RECEIVER_DEVICE,
    #                              "device_airpro", "STATS", 5, 0, KAFKA_TOPIC_DEVICE))
    # f2 = AppBrokerClient(SubsDto(MQTT_TOPIC_RECEIVER_NEIGHBOURS,
    #                              "neighbours_airpro", "STATS", 5, 0, KAFKA_TOPIC_NEIGHBOURS))
    f3 = AppBrokerClient(SubsDto(MQTT_TOPIC_RECEIVER_VIF,
                                 "vif_airpro", "STATS", 5, 0, KAFKA_TOPIC_VIF))

    # f4 = AppBrokerClient(SubsDto(MQTT_TOPIC_RECEIVER_VIF,
    #                              "vif_airpro", "STATS", 5, 0, KAFKA_TOPIC_CLIENTS))
    # f1.join_thread()
    # f2.join_thread()
    f3.join_thread()
    # f4.join_thread()
    logger.info("Server Started")
