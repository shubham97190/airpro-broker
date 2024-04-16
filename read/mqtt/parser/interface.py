import json
import logging
import zlib
from abc import abstractmethod
from protobuf.aircnms_stats_pb2 import Report

from google.protobuf.json_format import MessageToJson, MessageToDict

logger = logging.getLogger(__name__)


class ParserInterface:

    def __init__(self, report: Report):
        self.report = report

    @abstractmethod
    def deserialize(self):
        pass

    @abstractmethod
    def serialize(self):
        pass

    def extract_data(self, payload):
        try:
            decode_data = self.unzip_payload(payload)
            # bytes_data = self.extract_json_bytes(decode_data)
            return self.message_to_dictionary(decode_data)
        except Exception as error:
            logger.error("An exception occurred:", type(error).__name__, "–", error)
            # An exception occurred: division by zero

    def unzip_payload(self, payload: str):
        decompressed_data = zlib.decompress(payload)
        logger.info("decompressed data %s", decompressed_data)
        # decode_data = decompressed_data.decode()
        # logger.info("decode data %s", decode_data)
        return decompressed_data

    def extract_json_bytes(self, decode_data: str):
        json_data = json.loads(decode_data)
        logger.info("decode data %s", json_data)
        return bytes(json_data.data, "utf-8")

    def message_to_dictionary(self, json_bytes):
        self.report.ParseFromString(json_bytes)
        message_to_json = MessageToJson(self.report)
        # logger.info("decompressed json data  %s", message_to_json)
        return MessageToDict(self.report)
