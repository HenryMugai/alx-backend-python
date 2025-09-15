#!/usr/bin/env python3
import sqlite3

class ExecuteQuery:
    def __init__(self, db_name, query, params=()):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query, self.params)
        self.result = self.cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = (25,)
    with ExecuteQuery("users.db", query, params) as users:
        print("Users older than 25:", users)
