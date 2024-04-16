import json
import logging
import logging.config
import os.path
from os.path import exists

from dotenv import load_dotenv

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
    dto = SubsDto("airpro/cloud/to/dev/config", "test2", "CONFIG", 5, 1)
    f2 = AppBrokerClient(dto)
    dto1 = SubsDto("airpro/cloud/to/dev/stats", "test", "STATS", 5, 1)
    f1 = AppBrokerClient(dto1)
    f1.join_thread()
    f2.join_thread()
    logger.info("Server Started")
