from log import Log


class LogFileParser:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

        with open(self.log_file_path, "r") as log_file:
            self.log_file_line_count = sum(1 for _ in log_file.readlines())

    def parse_logs_file(self):
        with open(self.log_file_path, "r") as log_file:
            for line in log_file:
                yield Log.from_line(line)
