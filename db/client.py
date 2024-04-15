import requests

from db import exceptions
from db.connected_clients import ConnectedClient
from db.device import Device
from db.neighbors import Neighbor
from db.vif import VIF


class Client:
    BASE_URL = "http://127.0.0.1:8520/"

    def __init__(self, client_id=None, client_secret=None, domain=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.api_token = None
        self.vif = VIF(self)
        self.connected_client = ConnectedClient(self)
        self.device = Device(self)
        self.neighbor = Neighbor(self)

        if domain:
            if not domain.endswith("/"):
                domain += "/"
            self.BASE_URL = domain + "v1/"

    def set_access_token(self, access_token):
        self.access_token = access_token

    def set_api_token(self, api_token):
        self.api_token = api_token

    def _get(self, url, params=None, **kwargs):
        return self._request("get", url, params=params, **kwargs)

    def _post(self, url, **kwargs):
        return self._request("post", url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request("put", url, **kwargs)

    def _patch(self, url, **kwargs):
        return self._request("patch", url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request("delete", url, **kwargs)

    def _request(self, method, url, headers=None, params=None, **kwargs):
        _headers = {}
        _params = {}
        if self.access_token:
            _headers["Authorization"] = "Bearer {}".format(self.access_token)
        if self.api_token:
            _params["api_token"] = self.api_token
        if headers:
            _headers.update(headers)
        if params:
            _params.update(params)
        return self._parse(requests.request(method, url, headers=_headers, params=_params, **kwargs))

    def _parse(self, response):
        status_code = response.status_code
        if "Content-Type" in response.headers and "application/json" in response.headers["Content-Type"]:
            r = response.json()
        else:
            return response.text

        if not response.ok:
            error = None
            if "error" in r:
                error = r["error"]
            if status_code == 400:
                raise exceptions.BadRequestError(error, response)
            elif status_code == 401:
                raise exceptions.UnauthorizedError(error, response)
            elif status_code == 403:
                raise exceptions.ForbiddenError(error, response)
            elif status_code == 404:
                raise exceptions.NotFoundError(error, response)
            elif status_code == 410:
                raise exceptions.GoneError(error, response)
            elif status_code == 415:
                raise exceptions.UnsupportedMediaTypeError(error, response)
            elif status_code == 422:
                raise exceptions.UnprocessableEntityError(error, response)
            elif status_code == 429:
                raise exceptions.TooManyRequestsError(error, response)
            elif status_code == 500:
                raise exceptions.InternalServerError(error, response)
            elif status_code == 501:
                raise exceptions.NotImplementedError(error, response)
            elif status_code == 503:
                raise exceptions.ServiceUnavailableError(error, response)
            else:
                raise exceptions.UnknownError(error, response)

        return r
