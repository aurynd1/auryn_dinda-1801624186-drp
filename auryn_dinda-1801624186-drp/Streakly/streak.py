import sqlite3
from datetime import datetime

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


# =========================
# TAMBAH STREAK
# =========================
def tambah_streak():

    hari_ini = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT jumlah_hari, tanggal_terakhir
        FROM streak
    """)

    hasil = cursor.fetchone()

    if hasil is None:
        print("Data streak belum tersedia.")
        return

    jumlah_hari, tanggal_terakhir = hasil

    # Jika hari ini sudah pernah mendapat streak,
    # jangan tambah lagi
    if tanggal_terakhir == hari_ini:
        return

    # Jika belum pernah ada data streak
    if not tanggal_terakhir:
        jumlah_baru = 1

    else:

        terakhir = datetime.strptime(tanggal_terakhir, "%Y-%m-%d")
        hari_sekarang = datetime.strptime(hari_ini, "%Y-%m-%d")

        selisih = (hari_sekarang - terakhir).days

        # Jika berurutan (kemarin -> hari ini)
        if selisih == 1:
            jumlah_baru = jumlah_hari + 1

        # Jika ada hari yang terlewat
        elif selisih > 1:
            jumlah_baru = 1

        # Kondisi lain (misalnya tanggal di database lebih baru)
        else:
            jumlah_baru = jumlah_hari

    cursor.execute("""
        UPDATE streak
        SET
            jumlah_hari=?,
            tanggal_terakhir=?
    """, (jumlah_baru, hari_ini))

    conn.commit()

    # Hanya tampil jika streak benar-benar bertambah
    if jumlah_baru != jumlah_hari:
        print("Streak +1🔥")


# =========================
# RESET STREAK
# =========================
def reset_streak():

    cursor.execute("""
        UPDATE streak
        SET
            jumlah_hari=0,
            tanggal_terakhir=?
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