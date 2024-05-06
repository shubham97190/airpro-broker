import logging

from read.mqtt.parser.interface import ParserInterface

logger = logging.getLogger(__name__)


class ConfigParser(ParserInterface):

    def __init__(self):
        super(ConfigParser, self).__init__()

    def deserialize(self, payload, kf_topic):
        logger.info("Config Parser initiated for payload %s", payload)
        # message_to_dict = super(ConfigParser, self).extract_data(payload)
        # logger.info("Config Parser done for dict %s", message_to_dict)

    def serialize(self):
        pass
