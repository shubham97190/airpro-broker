from typing import Union
from dataclasses import dataclass, asdict, field
from json import dumps

@dataclass
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
    topic: str
    client_id: str
    key: str
    thread_count: int
    p_qos: int
    user_name: str = None
    passwd: str = None
    b_port: str = None
    broker_ip: str = None

@dataclass
class DeviceDto(SuperDataClass):
    serial_num: str
    device_id: str
    mac_addr: str

@dataclass
class StatisticsDto(SuperDataClass):
    device:str
    data: Union[dict, list]
    
