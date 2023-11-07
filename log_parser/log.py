import json
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from encoder import CustomJSONEncoder


class LogLevel(Enum):
    Info = 'INFO'
    Warning = 'WARNING'
    Error = 'ERROR'


@dataclass
class Log:
    timestamp: datetime
    level: LogLevel
    message: str

    def __str__(self):
        return json.dumps(vars(self), cls=CustomJSONEncoder)

    @classmethod
    def from_line(cls, line: str):
        json_line = json.loads(line)
        if json_line.keys() != vars(cls).keys():
            raise Exception(f'Invalid log format: {line}')
        return cls(**json_line)
