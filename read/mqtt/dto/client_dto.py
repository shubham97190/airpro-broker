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
