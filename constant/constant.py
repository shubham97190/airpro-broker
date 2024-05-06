from typing import Final


KAFKA_TOPIC_DEVICE: Final[str] = "device"
KAFKA_TOPIC_CLIENTS: Final[str] = "clients"
KAFKA_TOPIC_NEIGHBOURS: Final[str] = "neighbours"
KAFKA_TOPIC_VIF: Final[str] = "vif"

MQTT_TOPIC_RECEIVER_DEVICE: Final[str] = "/dev/to/cloud/+/+/device"
MQTT_TOPIC_RECEIVER_NEIGHBOURS: Final[str] = "/dev/to/cloud/+/+/neighbor"
MQTT_TOPIC_RECEIVER_VIF: Final[str] = "/dev/to/cloud/+/+/vif"
MQTT_TOPIC_RECEIVER_CLIENTS: Final[str] = "/dev/to/cloud/+/+/client"
