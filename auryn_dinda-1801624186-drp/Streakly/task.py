import sqlite3
conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()
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
def tambah_tugas():def 
    nama = input("Masukkan tugas: ")
    tugas.append(nama)
    print("Tugas berhasil ditambahkan.")

def lihat_tugas():
    for i, t in enumerate(tugas, 1):
        print(f"{i}. {t}")