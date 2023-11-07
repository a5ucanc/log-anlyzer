import datetime
from pathlib import Path
from log_analyzer.log_parser.log import Log, LogLevel
import random


def generate_dummy_log_file(file_path, num_entries=10000):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as log_file:
        for _ in range(num_entries):
            # Generate a random timestamp
            timestamp = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 86400))
            log_level = random.choice(list(LogLevel))
            message = f"Random log message: {random.randint(1, 100)}"
            log_file.write(str(Log(timestamp, log_level, message)) + '\n')

