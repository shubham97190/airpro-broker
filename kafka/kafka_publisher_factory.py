from kafka.client_producer import ClientProducer
from kafka.device_procuder import DeviceProducer
from kafka.neighbours_procuder import NeighboursProducer
from kafka.vif_procuder import VIFProducer


class KafkaPublisherFactory:

    def __init__(self):
        self._creators = {}

    def register_publisher(self, key, creator):
        self._creators[key] = creator

    def get_publisher(self, key):
        creator = self._creators.get(key)
        if not creator:
            raise ValueError(format)
        return creator()

    def get_all_creators(self):
        return self._creators


kf_client_factory = KafkaPublisherFactory()
kf_client_factory.register_publisher('device', DeviceProducer)
kf_client_factory.register_publisher('vif', VIFProducer)
kf_client_factory.register_publisher('neighbours', NeighboursProducer)
kf_client_factory.register_publisher('clients', ClientProducer)
