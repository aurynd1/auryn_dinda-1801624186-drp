import sqlite3
from datetime import datetime

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()

# =========================
# TAMBAH STREAK
# =========================
def tambah_streak():

    cursor.execute("""
        UPDATE streak
        SET
            jumlah_hari = jumlah_hari + 1,
            tanggal_terakhir = ?
    """, (datetime.now().strftime("%Y-%m-%d"),))

    conn.commit()

    print("Streak +1🔥")


# =========================
# RESET STREAK
# =========================
def reset_streak():

    cursor.execute("""
        UPDATE streak
        SET
            jumlah_hari = 0,
            tanggal_terakhir = ?
    """, (datetime.now().strftime("%Y-%m-%d"),))

    conn.commit()

    print("Streak direset menjadi 0🥺")
    print("Ayo semangat mempertahankan streakmu!😤")


# =========================
# LIHAT STREAK
# =========================
def lihat_streak():

    cursor.execute("""
        SELECT
            jumlah_hari,
            tanggal_terakhir
        FROM streak
    """)

    hasil = cursor.fetchone()

    if hasil:

        print("\n===== STREAK =====")
        print(f"Jumlah Hari : {hasil[0]}")
        print(f"Terakhir Update : {hasil[1]}")

    else:

        print("Data streak belum tersedia.")