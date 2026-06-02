# IF STATEMENT

# - Menggunakan sintaks "if"
# - Sintaks (if <boolean>)
# - Di dalam alur if harus terdapat indentasi secara koding

def check_tujuan(terdesak=False):
    # nilai default terdesak = False
    if terdesak:
        # perintah di dalam ini hanya akan berfungsi hanya jika nilai terdesak = True
        tujuan = 'kampus'
    else:
        # perintah di dalam ini hanya akan berfungsi hanya jika nilai terdesak = False
        tujuan = 'stasiun'

    return tujuan

# Alternatif penulisan if statement
# menggunakan nilai default
# praktek yang lebih baik, karena lebih efisien

def check_tujuan2(terdesak):
    tujuan = 'stasiun'  # nilai default dari tujuan

    if terdesak:
        # perintah di dalam ini hanya akan berfungsi hanya jika nilai terdesak = True
        tujuan = 'kampus'

    # OUT
    return tujuan

# setelah if tidak harus secara gamblang mengevaluasikan langsung true-false
# if False:
#     print('Apakah tulisan ini muncul?')
# alternatifnya, kita bisa menggunakan operator logika

# Tabel kebenaran
# - AND
#     A  |   B    |   OUTPUT
# ----------------------------
#     v  |   v    |     v
#     v  |   x    |     x
#     x  |   v    |     x
#     x  |   x    |     x

# - OR
#     A  |   B    |   OUTPUT
# ----------------------------
#     v  |   v    |     v
#     v  |   x    |     v
#     x  |   v    |     v
#     x  |   x    |     x

# - NOT (penegasian, not A)
#     A    |   OUTPUT
# ----------------------------
#     v    |     x
#     x    |     v

# misal:
# 1. Hujan dan berangin
# 2. Hujan atau berangin

# OPERASI AND (A and B)
# 1. Jika hujan dan berangin, maka saya tetap di rumah
# 2. Hari ini hujan dan tidak berangin
# 3. Saya tidak tetap di rumah (stay = False)

# OPERASI OR (A or B)
# 1. Jika hujan atau berangin, maka saya tetap di rumah
# 2. Hari ini hujan dan tidak berangin
# 3. Saya tetap di rumah (stay = True)

def is_stay(hujan, berangin):
    if hujan and berangin: # Jika hujan dan berangin
        stay = True # saya tetap di rumah
    else:
        stay = False

    return stay

# selain operator logika, bisa juga menggunakan operator pembanding jika pengkondisian bergantung dengan angka
# operator pembanding membandingkan satu angka dengan yang lain
# contoh operator pembanding
# 1. == (sama dengan)
# 2. < (kurang dari)
# 3. > (lebih dari)
# 4. <= (kurang dari atau sama dengan)
# 5. >= (lebih besar atau sama dengan)
# operator pembanding ekslusif untuk penggunaan angka (tipe data selain angka tidak berfungsi/error)
# contoh penggunaan operator pembanding:
# 3 == 4 (3 sama dengan 4) -> menghasilkan logika False
# digunakan jika sudah menggunakan angka dalam proses pengkondisian
# hasil dari operator pembanding adalah boolean

# deklarasi variabel nilai
def f4():
    nilai = 70

    # jika nilai = 70, maka beri notifikasi "nilai ngepas!"
    if nilai == 70:
        print('nilai ngepas')

    # jika nilai kurang dari 70, maka beri notifikasi "tidak lulus"
    if nilai < 70:
        print('tidak lulus')
    else:
        print('selamat anda lulus')

# implementasi fungsi untuk konversi nilai angka ke nilai huruf (A, A-, B+)
# 86-100 A 4
# 81-85 A- 3,7
# 76-80 B+ 3,3
# 71-75 B 3,0
# 66-70 B- 2,7

# 61-65 C+ 2,3
# 56-60 C 2,0
# 51-55 C- 1,7
# 46-50 D 1
# 0-45 E 0

# gunakan "elif" untuk pengkondisian lebih dari 2

nilai = int(input('Masukkan nilai: '))

is_lulus = nilai >= 70
if is_lulus:
    print('anda lulus')

if nilai <= 45:
    # jika tidak terpenuhi, maka pengkondisian akan dilempar ke elif
    huruf = 'E'
elif nilai <= 50:
    # jika if sudah terpenuhi, maka fungsi ini tidak dijalankan
    huruf = 'D'
elif nilai <= 55:
    huruf = 'C-'
else:
    huruf = 'A'

print(huruf)