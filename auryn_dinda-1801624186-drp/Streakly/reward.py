import sqlite3
from datetime import datetime

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


# =========================
# CREATE
# =========================
def tambah_reward():

    nama = input("Nama Reward : ")
    deskripsi = input("Deskripsi : ")

    status = "aktif"
    poin = 50

    cursor.execute("""
        INSERT INTO reward
        (nama_reward, deskripsi, status, poin_dibutuhkan)
        VALUES (?, ?, ?, ?)
    """, (nama, deskripsi, status, poin))

    conn.commit()

    print("Reward berhasil ditambahkan.")


# =========================
# READ
# =========================
def lihat_reward():

    cursor.execute("""
        SELECT rowid, nama_reward, deskripsi, status
        FROM reward
    """)

    data = cursor.fetchall()

    print("\n===== DAFTAR REWARD =====")

    if len(data) == 0:
        print("Belum ada reward.")
        return

    for d in data:

        print(f"ID : {d[0]}")
        print(f"Reward : {d[1]}")
        print(f"Deskripsi : {d[2]}")
        print("Poin Penukaran : 50 poin")
        print(f"Status : {d[3]}")
        print("------------------------")


# =========================
# UPDATE
# =========================
def edit_reward():

    lihat_reward()

    id_reward = int(input("Masukkan ID Reward : "))

    nama = input("Nama Reward Baru : ")
    deskripsi = input("Deskripsi Baru : ")
    status = input("Status (aktif/non aktif): ")

    cursor.execute("""
        UPDATE reward
        SET
            nama_reward=?,
            deskripsi=?,
            status=?,
            poin_dibutuhkan=50
        WHERE rowid=?
    """, (nama, deskripsi, status, id_reward))

    conn.commit()

    print("Reward berhasil diperbarui.")


# =========================
# DELETE
# =========================
def hapus_reward():

    lihat_reward()

    id_reward = int(input("Masukkan ID Reward : "))

    cursor.execute("""
        DELETE FROM reward
        WHERE rowid=?
    """, (id_reward,))

    conn.commit()

    print("Reward berhasil dihapus.")


# =========================
# TUKAR REWARD
# =========================
def tukar_reward():

    lihat_reward()

    cursor.execute("""
        SELECT jumlah_poin
        FROM point
    """)

    hasil = cursor.fetchone()

    if hasil is None:
        print("Data poin belum tersedia.")
        return

    jumlah_poin = hasil[0]

    print(f"\nPoin Anda : {jumlah_poin}")

    id_reward = int(input("\nPilih ID Reward : "))

    cursor.execute("""
        SELECT nama_reward
        FROM reward
        WHERE rowid=?
    """, (id_reward,))

    reward = cursor.fetchone()

    if reward is None:
        print("Reward tidak ditemukan.")
        return

    nama_reward = reward[0]

    if jumlah_poin >= 50:

        cursor.execute("""
            INSERT INTO penukaran_reward
            (reward, tanggal_penukaran, poin_digunakan)
            VALUES (?, ?, ?)
        """, (
            nama_reward,
            datetime.now().strftime("%Y-%m-%d"),
            50
        ))

        cursor.execute("""
            UPDATE point
            SET jumlah_poin = jumlah_poin - 50
        """)

        conn.commit()

        cursor.execute("""
            SELECT jumlah_poin
            FROM point
        """)

        sisa_poin = cursor.fetchone()[0]

        print("\n========================")
        print("Reward berhasil ditukar!")
        print(f"Reward : {nama_reward}")
        print(f"Sisa Poin : {sisa_poin}")
        print("========================")

    else:

        print("\nYah, poinmu belum mencukupi😔")
        print("\nAyo kerjakan seluruh task yang ada untuk menambah poin!🤩")
        print(f"Poin Anda : {jumlah_poin}")
        print("Minimal poin : 50 poin")