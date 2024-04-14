from read.mqtt.parser.config_parser import ConfigParser
from read.mqtt.parser.statistics_parser import StatisticsParser


class ParserFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, payload_parser, creator):
        self._creators[payload_parser] = creator

    def get_serializer(self, payload_parser):
        creator = self._creators.get(payload_parser)
        if not creator:
            raise ValueError(format)
        return creator()


factory = ParserFactory()
factory.register_format('CONFIG', ConfigParser)
factory.register_format('STATS', StatisticsParser)
