tugas = []

def tambah_tugas():
    nama = input("Masukkan tugas: ")
    tugas.append(nama)
    print("Tugas berhasil ditambahkan.")

def lihat_tugas():
    for i, t in enumerate(tugas, 1):
        print(f"{i}. {t}")