from typing import Union
from dataclasses import dataclass, asdict, field
from json import dumps

@dataclass(frozen=True)
class SubsDto:
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
class StatisticsDto:
    serial_num: str
    device_id: str
    mac_addr: str
    data: Union[dict, list]
    
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
