import json
import logging

from db.client import Client

logger = logging.getLogger(__name__)


class DBInterface:
    def __init__(self, url):
        self.url = url
        self._client = Client()

    def get(self, key_id, **kwargs):
        url = "{}/{}".format(self.url, key_id)
        logger.info("get %s", url)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all(self, params=None, **kwargs):
        logger.info("get all %s", self.url)
        return self._client._get(self._client.BASE_URL + self.url, params=params, **kwargs)

    def create(self, data, **kwargs):
        logger.info("create %s %s", self.url, data)
        return self._client._post(self._client.BASE_URL + self.url, json=data, **kwargs)

    def update(self, key_id, data, **kwargs):
        url = "{}/{}".format(self.url, key_id)
        logger.info("update %s", self.url)
        return self._client._put(self._client.BASE_URL + self.url, json=data, **kwargs)

    def delete(self, key_id, **kwargs):
        url = "{}/{}".format(self.url, key_id)
        logger.info("delete %s", url)
        return self._client._delete(self._client.BASE_URL + self.url, **kwargs)
