import sqlite3

class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def disconnect(self, exc_type=None, exc_val=None, exc_tb=None):
        if exc_type is None:
            self.conn.commit()
        self.conn.close()