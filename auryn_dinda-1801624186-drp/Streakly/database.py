import sqlite3

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()

# =========================
# TABEL TASK
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_tugas TEXT NOT NULL,
    status TEXT DEFAULT 'Belum Selesai',
    tanggal_selesai TEXT
)
""")

# =========================
# TABEL POINT
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS point(
    jumlah_poin INTEGER
)
""")

# =========================
# TABEL STREAK
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS streak(
    jumlah_hari INTEGER,
    tanggal_terakhir TEXT
)
""")

# =========================
# TABEL REWARD
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS reward(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_reward TEXT,
    deskripsi TEXT,
    status TEXT,
    poin_dibutuhkan INTEGER
)
""")

# =========================
# TABEL PENUKARAN REWARD
# =========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS penukaran_reward(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    reward TEXT,
    tanggal_penukaran TEXT,
    poin_digunakan INTEGER
)
""")

# =========================
# DATA AWAL POINT
# =========================
cursor.execute("SELECT COUNT(*) FROM point")

if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO point
    VALUES (0)
    """)

# =========================
# DATA AWAL STREAK
# =========================
cursor.execute("SELECT COUNT(*) FROM streak")

if cursor.fetchone()[0] == 0:
    cursor.execute("""
    INSERT INTO streak
    VALUES (0,'')
    """)

conn.commit()
conn.close()

print("Database berhasil dibuat.")