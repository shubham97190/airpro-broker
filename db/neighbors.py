import logging
logger = logging.getLogger(__name__)

class Neighbor(object):
    def __init__(self, client):
        self._client = client
    
    def get_neighbor(self, neighbor_id, **kwargs):
        url = "neighbor/{}".format(neighbor_id)
        logger.info("get neighbor %s", url)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_neighbors(self, params=None, **kwargs):
        url = "neighbor"
        logger.info("get neighbor")
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_neighbor(self, data, **kwargs):
        url = "neighbor"
        logger.info("create neighbor")
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_neighbor(self, neighbor_id, data, **kwargs):
        url = "neighbor/{}".format(neighbor_id)
        logger.info("update neighbor %s", url)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_neighbor(self, neighbor_id, **kwargs):
        url = "neighbor/{}".format(neighbor_id)
        logger.info("delete neighbor %s", url)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)