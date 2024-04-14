import logging

from read.mqtt.base.base_mqtt_client import BaseMqttClient
from read.mqtt.base.base_subscriber import BaseSubscriber
from read.mqtt.dto.client_dto import SubsDto

logger = logging.getLogger(__name__)


class AppBrokerClient(BaseSubscriber):

    def __init__(self, dto: SubsDto):
        self.dto = dto

        super(AppBrokerClient, self).__init__(dto, self.get_client())
        self.start_thread()
        logger.info("Config broker initialized for topic %s", self.dto.topic)

    def join_thread(self):
        super(AppBrokerClient, self).join()

    def get_client(self):
        ap_client = BaseMqttClient(self.dto)
        return ap_client.connect_to_broker()

    def start_thread(self):
        super(AppBrokerClient, self).start()
