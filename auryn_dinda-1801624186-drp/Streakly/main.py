from task import tambah_tugas, lihat_tugas
from reward import (
    tambah_reward,
    lihat_reward,
    edit_reward,
    hapus_reward,
    tukar_reward
)
from points import lihat_poin
from streak import lihat_streak

while True:
    print("\n===== STREAKLY =====")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Reward")
    print("4. Lihat Poin")
    print("5. Lihat Streak")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_tugas()

    elif pilihan == "2":
        lihat_tugas()

    elif pilihan == "3":

        while True:

            print("\n===== MENU REWARD =====")
            print("1. Tambah Reward")
            print("2. Lihat Reward")
            print("3. Edit Reward")
            print("4. Hapus Reward")
            print("5. Tukar Reward")
            print("6. Kembali")

            pilih_reward = input("Pilih menu reward: ")

            if pilih_reward == "1":
                tambah_reward()

            elif pilih_reward == "2":
                lihat_reward()

            elif pilih_reward == "3":
                edit_reward()

            elif pilih_reward == "4":
                hapus_reward()

            elif pilih_reward == "5":
                tukar_reward()

            elif pilih_reward == "6":
                break

            else:
                print("Pilihan tidak tersedia.")

    elif pilihan == "4":
        lihat_poin()

    elif pilihan == "5":
        lihat_streak()

    elif pilihan == "6":
        print("Terima kasih telah menggunakan Streakly.")
        break

    else:
        print("Pilihan tidak tersedia.")