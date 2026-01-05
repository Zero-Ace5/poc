import sqlite3

conn = sqlite3.connect("logs.db")
cur = conn.cursor()

rows = cur.execute("SELECT * FROM git_logs").fetchall()

for r in rows:
    print(r)

conn.close()
