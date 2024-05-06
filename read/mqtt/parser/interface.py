import logging
from abc import abstractmethod

logger = logging.getLogger(__name__)


class ParserInterface:

    @abstractmethod
    def deserialize(self):
        pass

    @abstractmethod
    def serialize(self):
        pass
