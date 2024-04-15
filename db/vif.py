import logging
logger = logging.getLogger(__name__)

class VIF(object):
    def __init__(self, client):
        self._client = client
    
    def get_vif(self, vif_id, **kwargs):
        url = "vif/{}".format(vif_id)
        logger.info("get vif %s",url)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_vifs(self, params=None, **kwargs):
        url = "vif"
        logger.info("get all vif")
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_vif(self, data, **kwargs):
        url = "vif"
        logger.info("create vif")
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_vif(self, vif_id, data, **kwargs):
        url = "vif/{}".format(vif_id)
        logger.info("update vif %s", url)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_vif(self, vif_id, **kwargs):
        url = "vif/{}".format(vif_id)
        logger.info("delete vif %s", url)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)


