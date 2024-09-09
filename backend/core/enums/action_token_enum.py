from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    SOCKET = (
        'socket',
        timedelta(seconds=40)
    )

    def __init__(self, token_type, lifetime):
        self.token_type = token_type
        self.lifetime = lifetime
