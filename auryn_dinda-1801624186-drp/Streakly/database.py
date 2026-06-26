import sqlite3

conn = sqlite3.connect("streakly.db")

cursor = conn.cursor()

print("Database berhasil dibuat")

conn.close()