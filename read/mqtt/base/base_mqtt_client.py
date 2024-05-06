import logging
import os

import paho.mqtt.client as paho

from read.mqtt.dto.client_dto import SubsDto

logger = logging.getLogger(__name__)


class BaseMqttClient(paho.Client):

    def __init__(self, dto: SubsDto) -> None:
        self.mqtt_c = None
        self.broker_ip = dto.broker_ip if dto.broker_ip else os.getenv("MQTT_SERVER_BROKER_IP")
        self.user = dto.user_name if dto.user_name else os.getenv("MQTT_SERVER_USERNAME")
        self.passw = dto.passwd if dto.passwd else os.getenv("MQTT_SERVER_PASSWORD")
        self.broker_port = int(dto.b_port if dto.b_port else os.getenv("MQTT_SERVER_PORT"))
        self.client_id = dto.client_id
        self.topic = dto.mqtt_rec_topic
        self.qos = dto.p_qos
        super(BaseMqttClient, self).__init__(paho.CallbackAPIVersion.VERSION2, self.client_id)
        logger.info("config Set [%s]", self.broker_ip)

    def connect_to_broker(self):
        self.username_pw_set(self.user, self.passw)
        self.connect(self.broker_ip, self.broker_port, 60)
        self.on_connect = self.on_connect
        self.on_log = self.on_log
        self.on_disconnect = self.on_disconnect
        # mqtt_c.socket().setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)
        logger.info("connected to broker %s", self.broker_ip)
        return self

    def on_connect(self, client, obj, flags, reason_code, properties):
        if reason_code == 0:
            client.subscribe(self.topic, self.qos)
            logger.info("Subscribed successfully %s reason Code %s", self.topic, reason_code)
        else:
            logger.info("Subscribe to topic %s failed Returned code = %s", self.topic, reason_code)

    def on_log(self, client, obj, level, string):
        logger.info("message log %s", string)

    def on_disconnect(self, client, userdata, flags, reason_code, properties):
        logger.info("disconnect reason code %s, user data %s", reason_code, userdata)
        # self.disconnect.set_result(reason_code)
