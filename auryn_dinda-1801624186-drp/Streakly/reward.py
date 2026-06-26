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
    poin = int(input("Poin Dibutuhkan : "))
    status = "aktif"

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
        SELECT rowid, nama_reward, deskripsi, status, poin_dibutuhkan
        FROM reward
    """)

    data = cursor.fetchall()

    print("\n===== DAFTAR REWARD =====")

    for d in data:
        print(
            f"ID: {d[0]} | "
            f"Reward: {d[1]} | "
            f"Poin: {d[4]} | "
            f"Status: {d[3]}"
        )


# =========================
# UPDATE
# =========================
def edit_reward():

    id_reward = int(input("Masukkan ID Reward : "))

    nama = input("Nama Reward Baru : ")
    deskripsi = input("Deskripsi Baru : ")
    status = input("Status (aktif/non aktif): ")
    poin = int(input("Poin Dibutuhkan : "))

    cursor.execute("""
        UPDATE reward
        SET
            nama_reward=?,
            deskripsi=?,
            status=?,
            poin_dibutuhkan=?
        WHERE rowid=?
    """, (nama, deskripsi, status, poin, id_reward))

    conn.commit()

    print("Reward berhasil diperbarui.")


# =========================
# DELETE
# =========================
def hapus_reward():

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

    id_reward = int(input("\nPilih ID Reward : "))

    # Ambil poin user
    cursor.execute("""
        SELECT jumlah_poin
        FROM point
    """)

    hasil = cursor.fetchone()

    if hasil is None:
        print("Data poin belum tersedia.")
        return

    jumlah_poin = hasil[0]

    # Ambil reward yang dipilih
    cursor.execute("""
        SELECT
            nama_reward,
            poin_dibutuhkan
        FROM reward
        WHERE rowid=?
    """, (id_reward,))

    reward = cursor.fetchone()

    if reward is None:
        print("Reward tidak ditemukan.")
        return

    nama_reward = reward[0]
    poin_reward = reward[1]

    if jumlah_poin >= poin_reward:

        # Simpan riwayat penukaran
        cursor.execute("""
            INSERT INTO penukaran_reward
            (reward, tanggal_penukaran, poin_digunakan)
            VALUES (?, ?, ?)
        """, (
            nama_reward,
            datetime.now().strftime("%Y-%m-%d"),
            poin_reward
        ))

        # Reset poin menjadi 0
        cursor.execute("""
            UPDATE point
            SET jumlah_poin = 0
        """)

        conn.commit()

        print("\nReward berhasil ditukar!")
        print("Poin Anda sekarang menjadi 0.")

    else:
        print("\nPoin belum mencukupi.")
        print(f"Poin Anda : {jumlah_poin}")
        print(f"Dibutuhkan : {poin_reward}")