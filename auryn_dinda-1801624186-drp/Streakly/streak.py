import sqlite3
from datetime import datetime

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


# Menambah streak jika semua task selesai
def tambah_streak():

    cursor.execute("""
        UPDATE streak
        SET jumlah_hari = jumlah_hari + 1,
            tanggal_terakhir = ?
    """, (datetime.now().strftime("%Y-%m-%d"),))

    conn.commit()

    print("Streak bertambah 1 hari.")


# Reset streak jika ada task yang belum selesai
def reset_streak():

    cursor.execute("""
        UPDATE streak
        SET jumlah_hari = 0,
            tanggal_terakhir = ?
    """, (datetime.now().strftime("%Y-%m-%d"),))

    conn.commit()

    print("Streak direset menjadi 0.")


# Melihat streak
def lihat_streak():

    cursor.execute("""
        SELECT jumlah_hari
        FROM streak
    """)

    hasil = cursor.fetchone()

    if hasil:
        print(f"Streak Saat Ini : {hasil[0]} hari")
    else:
        print("Data streak belum tersedia.")