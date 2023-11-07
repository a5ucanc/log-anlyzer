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
        self.conn.close()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datetime TEXT,
                level TEXT,
                message TEXT
            )
        ''')

    def insert(self, datetime, level, message):
        self.cursor.execute('''
            INSERT INTO logs (datetime, level, message)
            VALUES (?, ?, ?)
        ''', (datetime, level, message))
        self.conn.commit()

    def select(self, level=None, message=None, datetime=None):
        query = 'SELECT * FROM logs'
        params = []
        if level:
            query += ' WHERE level = ?'
            params.append(level)
        if message:
            query += ' WHERE message LIKE ?'
            params.append(f'%{message}%')
        if datetime:
            query += ' WHERE datetime LIKE ?'
            params.append(f'%{datetime}%')
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def delete(self, id):
        self.cursor.execute('DELETE FROM logs WHERE id = ?', (id,))
        self.conn.commit()

    def delete_all(self):
        self.cursor.execute('DELETE FROM logs')
        self.conn.commit()
