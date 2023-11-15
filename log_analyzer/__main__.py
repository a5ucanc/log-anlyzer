import argparse
from collections import deque
from .log_parser.log_parser import LogParser
from .db import Database


def parse_logs(log_file_paths):
    with Database() as db:
        db.create_table()
        for log_file_path in log_file_paths:
            log_parser = LogParser(log_file_path)
            parsed_logs = log_parser.parse_logs()
            deque(map(lambda log: db.insert(**log.to_db()), parsed_logs))


def clear_cache():
    with Database() as db:
        db.delete_all()


def cache():
    pass


parser = argparse.ArgumentParser(description="Log Analyzer")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--logs', '-l', help='Path to log files', type=str, nargs='+')
group.add_argument('--cache', '-c', help='Use already parsed logs', action='store_true')
group.add_argument('--clear-cache', help='Clear cache', action='store_true')

args = parser.parse_args()

if args.logs:
    parse_logs(args.logs)
elif args.cache:
    cache()
elif args.clear_cache:
    clear_cache()
