import logging
logger = logging.getLogger(__name__)

class Device(object):
    def __init__(self, client):
        self._client = client
    
    def get_device(self, device_id, **kwargs):
        url = "device/{}".format(device_id)
        logger.info("get device %s", url)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_devices(self, params=None, **kwargs):
        url = "device"
        logger.info("get all devices")
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def create_device(self, data, **kwargs):
        url = "device"
        logger.info("create device %s", url)
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_device(self, device_id, data, **kwargs):
        url = "device/{}".format(device_id)
        logger.info("update device %s", url)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_device(self, device_id, **kwargs):
        url = "device/{}".format(device_id)
        logger.info("delete device %s", url)
        return self._client._delete(self._client.BASE_URL + url, **kwargs)


