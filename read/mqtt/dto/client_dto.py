from typing import Union
from dataclasses import dataclass


@dataclass(frozen=True)
class SubsDto:
    topic: str
    client_id: str
    key: str
    thread_count: int
    user_name: str = None
    passwd: str = None
    b_port: str = None
    broker_ip: str = None

@dataclass(frozen=True)
class StatisticsDto:
    serial_num: str
    device_id: str
    mac_addr: str
    data: Union[dict, list]
    