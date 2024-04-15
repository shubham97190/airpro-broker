
import logging
logger = logging.getLogger(__name__)

class ConnectedClient(object):
    def __init__(self, client):
        self._client = client
    
    def get_client(self, client_id, **kwargs):
        url = "client/{}".format(client_id)
        logger.info("get client %s", url)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_clients(self, params=None, **kwargs):
        url = "client"
        logger.info("get all clients")
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_client(self, data, **kwargs):
        url = "client"
        logger.info("create clients")
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_client(self, client_id, data, **kwargs):
        url = "client/{}".format(client_id)
        logger.info("update client %s", url)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_client(self, client_id, **kwargs):
        url = "client/{}".format(client_id)
        logger.info("delete client %s", url)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)


