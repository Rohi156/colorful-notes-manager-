import sqlite3

conn = sqlite3.connect('database.db')  # database file तयार होईल
conn.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    color TEXT NOT NULL
);
''')
conn.close()
print("✅ Database तयार झाला.")
