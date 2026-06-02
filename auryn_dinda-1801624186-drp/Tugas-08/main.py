from datetime import datetime

# =================================
# SOAL 1 - PAPAN CATUR
# =================================

print("=== PAPAN CATUR ===\n")

for baris in range(8):
    for kolom in range(8):

        if (baris + kolom) % 2 == 0:
            print("⬜", end=" ")
        else:
            print("⬛", end=" ")

    print()

# =================================
# SOAL 2 - DATA AKTIVITAS
# =================================

print("\n=== PENDATAAN AKTIVITAS ===")

daftar_aktivitas = []

jumlah = int(input("Berapa aktivitas yang ingin diinput? "))

for i in range(jumlah):

    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Nama aktivitas : ")
    durasi = input("Durasi aktivitas (menit/jam) : ")
    status = input("Status kegiatan (done/not yet/ongoing) : ")

    # tanggal & waktu otomatis
    sekarang = datetime.now()

    tanggal = sekarang.strftime("%d/%m/%Y")
    waktu = sekarang.strftime("%H:%M:%S")

    # menyimpan data
    data = {
        "aktivitas": aktivitas,
        "durasi": durasi,
        "tanggal": tanggal,
        "waktu": waktu,
        "status": status
    }

    daftar_aktivitas.append(data)

# =================================
# OUTPUT
# =================================

print("\n=== DAFTAR AKTIVITAS ===")

for i, data in enumerate(daftar_aktivitas, start=1):

    print(f"""
Aktivitas {i}
-------------------------
Nama Aktivitas : {data['aktivitas']}
Durasi         : {data['durasi']}
Tanggal        : {data['tanggal']}
Waktu Input    : {data['waktu']}
Status         : {data['status']}
""")

print(f"Total aktivitas : {len(daftar_aktivitas)}")