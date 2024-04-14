import logging
import threading

from paho.mqtt.client import Client

from read.mqtt.dto.client_dto import SubsDto
from read.mqtt.parser.parser_factory import factory
from read.mqtt.thread.base_thread_pool import BaseThreadPool

logger = logging.getLogger(__name__)


class BaseSubscriber(threading.Thread):

    def __init__(self, dto: SubsDto, client: Client):
        super(BaseSubscriber, self).__init__()
        self.thread_name = f"{dto.key}_thread".lower()
        self.executor = BaseThreadPool(dto.thread_count, f"{self.thread_name}").get_thread_pool()
        self.name = self.thread_name
        self.daemon = True
        self.mqtt_c = client
        self.mqtt_c.on_message = self.on_message
        self.mqtt_c.on_subscribe = self.on_subscribe
        self.creator = factory.get_serializer(dto.key)

    def run(self):
        logger.info("new thread [%s] assigned to topic [%s]", self.name, self.dto.topic)
        self.subscribe()

    def subscribe(self):
        self.mqtt_c.loop_forever()

    def on_message(self, client, obj, msg):
        logger.info("Message received on topic [%s] qos [%s] and payload [%s] ", msg.topic, str(msg.qos),
                    str(msg.payload))
        s = self.executor.submit(self.creator.deserialize, msg.payload)
        logger.info("Parser Submitted %s ", s.done())

    def on_subscribe(self, client, obj, mid, reason_code_list, properties):
        logger.info("Subscribed: [%s], reason code list [%s]", str(mid), str(reason_code_list))
