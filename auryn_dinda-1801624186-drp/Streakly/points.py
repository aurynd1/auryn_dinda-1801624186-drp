import sqlite3

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


# Menambah 10 poin setiap task selesai
def tambah_poin():

    cursor.execute("""
        UPDATE point
        SET jumlah_poin = jumlah_poin + 10
    """)

    conn.commit()

    print("Poin berhasil ditambahkan (+10).")


# Melihat jumlah poin
def lihat_poin():

    cursor.execute("""
        SELECT jumlah_poin
        FROM point
    """)

    hasil = cursor.fetchone()

    if hasil:
        print(f"Jumlah Poin : {hasil[0]}")
    else:
        print("Data poin belum tersedia.")