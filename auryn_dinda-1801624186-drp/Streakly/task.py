import sqlite3

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")
conn.commit()

# =========================
# Fungsi Database (SQLite)
# =========================

def add_task(name):
    cursor.execute("INSERT INTO task (name) VALUES (?)", (name,))
    conn.commit()


def get_tasks():
    cursor.execute("SELECT * FROM task")
    return cursor.fetchall()


def update_task(id, name):
    cursor.execute("UPDATE task SET name=? WHERE id=?", (name, id))
    conn.commit()


def delete_task(id):
    cursor.execute("DELETE FROM task WHERE id=?", (id,))
    conn.commit()

# =========================
# Fungsi yang dipanggil main.py
# =========================

def tambah_tugas():
    nama = input("Masukkan tugas: ")
    add_task(nama)
    print("Tugas berhasil ditambahkan.")


def lihat_tugas():
    data = get_tasks()

    if not data:
        print("Belum ada tugas.")
    else:
        print("\n===== DAFTAR TUGAS =====")
        for tugas in data:
            print(f"{tugas[0]}. {tugas[1]}")