from db.base_device import BaseDevice
from db.connected_clients import ConnectedClient
from db.device import Device
from db.neighbors import Neighbor
from db.vif import VIF


class DBClientFactory:

    def __init__(self):
        self._creators = {}

    def register_db_client(self, key, creator):
        self._creators[key] = creator

    def get_db_client(self, key):
        creator = self._creators.get(key)
        if not creator:
            raise ValueError(format)
        return creator()

    def get_all_creators(self):
        return self._creators


db_client_factory = DBClientFactory()
db_client_factory.register_db_client('device', Device)
db_client_factory.register_db_client('vif', VIF)
db_client_factory.register_db_client('neighbors', Neighbor)
db_client_factory.register_db_client('clients', ConnectedClient)
db_client_factory.register_db_client('base-device', BaseDevice)
