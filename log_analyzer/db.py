import sqlite3

from . import config


# Context manager for database connection
class Database:
    def __init__(self):
        self.conn = sqlite3.connect(config.database)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                level TEXT,
                message TEXT
            )
        ''')

    def insert(self, timestamp, level, message):
        self.cursor.execute('''
            INSERT INTO logs (timestamp, level, message)
            VALUES (?, ?, ?)
        ''', (timestamp, level, message))



    def select(self, level=None, message=None, timestamp=None):
        query = 'SELECT * FROM logs'
        params = []
        if level:
            query += ' WHERE level = ?'
            params.append(level)
        if message:
            query += ' WHERE message LIKE ?'
            params.append(f'%{message}%')
        if timestamp:
            query += ' WHERE timestamp LIKE ?'
            params.append(f'%{timestamp}%')
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def delete(self, id):
        self.cursor.execute('DELETE FROM logs WHERE id = ?', (id,))

    def delete_all(self):
        self.cursor.execute('DELETE FROM logs')

    def commit(self):
        self.conn.commit()
