from task import tambah_tugas, lihat_tugas
from streak import lihat_streak
from points import lihat_poin
from reward import tukar_reward

while True:
    print("\n=== STREAKLY ===")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Lihat Streak")
    print("4. Lihat Poin")
    print("5. Tukar Reward")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":
        lihat_streak()

    elif pilihan == "4":
        lihat_poin()

    elif pilihan == "5":
        tukar_reward()

    elif pilihan == "6":
        break