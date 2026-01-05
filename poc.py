import sqlite3
import subprocess

conn = sqlite3.connect("logs.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS git_logs (
    commit_hash TEXT,
    author TEXT,
    date TEXT,
    message TEXT
)
""")

log_output = subprocess.check_output(
    ["git", "log", "--pretty=format:%H|%an|%ad|%s"],
    text=True
)

for line in log_output.splitlines():
    commit_hash, author, date, message = line.split("|", 3)
    cur.execute(
        "INSERT INTO git_logs VALUES (?, ?, ?, ?)",
        (commit_hash, author, date, message)
    )

conn.commit()
conn.close()

print("Git logs stored in database.")
