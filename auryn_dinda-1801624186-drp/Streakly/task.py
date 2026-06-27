import sqlite3
from datetime import datetime
from points import tambah_poin
from streak import tambah_streak

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


# =========================
# CREATE
# =========================
def tambah_tugas():

    nama = input("Masukkan nama tugas: ")

    cursor.execute("""
        INSERT INTO task
        (nama_tugas)
        VALUES (?)
    """, (nama,))

    conn.commit()

    print("Tugas berhasil ditambahkan.")


# =========================
# READ
# =========================
def lihat_tugas():

    cursor.execute("""
        SELECT
            id,
            nama_tugas,
            status
        FROM task
    """)

    data = cursor.fetchall()

    if len(data) == 0:
        print("Belum ada tugas.")
        return

    print("\n===== DAFTAR TUGAS =====")

    for d in data:

        print(
            f"ID : {d[0]} | "
            f"Tugas : {d[1]} | "
            f"Status : {d[2]}"
        )

# =========================
# UPDATE
# =========================
def selesaikan_tugas():

    lihat_tugas()

    try:

        id_task = int(input("\nMasukkan ID tugas yang selesai : "))

        cursor.execute("""
            SELECT status
            FROM task
            WHERE id=?
        """, (id_task,))

        hasil = cursor.fetchone()

        if hasil is None:
            print("ID tugas tidak ditemukan.")
            return

        if hasil[0] == "Selesai":
            print("Tugas sudah selesai.")
            return

        cursor.execute("""
            UPDATE task
            SET
                status='Selesai',
                tanggal_selesai=?
            WHERE id=?
        """, (
            datetime.now().strftime("%Y-%m-%d"),
            id_task
        ))

        conn.commit()

        tambah_poin()
        tambah_streak()

        print("Tugas berhasil diselesaikan.")

    except ValueError:
        print("Masukkan ID berupa angka.")
# =========================
# DELETE
# =========================
def hapus_tugas():

    lihat_tugas()

    id_task = int(input("\nMasukkan ID tugas yang akan dihapus : "))

    cursor.execute("""
        DELETE FROM task
        WHERE id=?
    """, (id_task,))

    conn.commit()

    print("Tugas berhasil dihapus.")