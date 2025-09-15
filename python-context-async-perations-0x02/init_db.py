#!/usr/bin/env python3
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table with age column
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    age INTEGER
)
""")

# Clear old data
cursor.execute("DELETE FROM users")

# Insert sample users
cursor.executemany("""
INSERT INTO users (name, email, age) VALUES (?, ?, ?)
""", [
    ("Alice", "alice@example.com", 30),
    ("Bob", "bob@example.com", 45),
    ("Charlie", "charlie@example.com", 50),
])

conn.commit()
conn.close()
print("users.db initialized with sample data.")
