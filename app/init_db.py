import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
conn.commit()
conn.close()
