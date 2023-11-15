from datetime import datetime
from enum import Enum

from . import config


def convert_types(mapping: dict, data: dict):
    """Converts types of values in data according to mapping"""
    for key, value in data.items():
        if key in mapping:
            data[key] = convert(value, mapping[key])
        else:
            raise TypeError
    return data


def convert(value, data_type):
    match data_type:
        case d if d == datetime:
            if config.time_format:
                return datetime.strptime(value, config.time_format)
            else:
                return datetime.fromisoformat(value)
        case _:
            return data_type(value)


def encode(value):
    """Encodes values to db friendly types"""
    match value:
        case d if isinstance(d, datetime):
            if config.time_format:
                return value.strftime(config.time_format)
            else:
                return value.isoformat()
        case d if isinstance(d, Enum):
            return value.value
        case _:
            return value
