from dataclasses import dataclass, asdict
from json import dumps
from typing import Union


@dataclass(frozen=True)
class SuperDataClass:

    @property
    def __dict__(self):
        """
        get a python dictionary
        """
        return asdict(self)

    @property
    def json(self):
        """
        get the json formated string
        """
        return dumps(self.__dict__)


@dataclass(frozen=True)
class SubsDto(SuperDataClass):
    mqtt_rec_topic: str
    client_id: str
    key: str
    thread_count: int
    p_qos: int
    kf_pub_topic: str
    user_name: str = None
    passwd: str = None
    b_port: str = None
    broker_ip: str = None


@dataclass(frozen=True)
class StatisticsDto(SuperDataClass):
    serial_num: str
    device_id: str
    mac_addr: str
    data: Union[dict, list]
