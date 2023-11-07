import json
from datetime import datetime
from enum import Enum


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value  # Serialize the Enum as its string value
        elif isinstance(obj, datetime):
            return obj.isoformat()  # Serialize the datetime as ISO format string
        return super().default(obj)
