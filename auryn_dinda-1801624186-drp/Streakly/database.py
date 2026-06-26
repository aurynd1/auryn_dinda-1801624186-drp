import sqlite3

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()

# =========================
# TABLE TASK
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# =========================
# TABLE REWARD
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS reward(
    nama_reward TEXT,
    deskripsi TEXT,
    status TEXT,
    poin_dibutuhkan INTEGER
)
""")

# =========================
# TABLE POINT
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS point(
    jumlah_poin INTEGER
)
""")

# =========================
# TABLE STREAK
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS streak(
    jumlah_hari INTEGER,
    tanggal_terakhir TEXT
)
""")

conn.commit()
conn.close()

print("Database berhasil dibuat.")