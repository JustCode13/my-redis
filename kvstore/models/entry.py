from dataclasses import dataclass
from typing import Any

@dataclass
class Entry:
    # key: str
    value: Any
    created_at: float
    expired_at: float | None
    metadata: dict[str,Any]

    def to_dict(self):
        return self.__dict__