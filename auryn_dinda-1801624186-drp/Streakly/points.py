import sqlite3

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()

# =========================
# TAMBAH POIN
# =========================
def tambah_poin():

    cursor.execute("""
        UPDATE point
        SET jumlah_poin = jumlah_poin + 10
    """)

    conn.commit()

    print("+10 poin berhasil ditambahkan.")


# =========================
# LIHAT POIN
# =========================
def lihat_poin():

    cursor.execute("""
        SELECT jumlah_poin
        FROM point
    """)

    hasil = cursor.fetchone()

    if hasil:
        print(f"\nJumlah Poin : {hasil[0]}")

    else:
        print("Data poin belum tersedia.")