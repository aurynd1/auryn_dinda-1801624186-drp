from task import (
    tambah_tugas,
    lihat_tugas,
    selesaikan_tugas,
    hapus_tugas
)

from reward import (
    tambah_reward,
    lihat_reward,
    edit_reward,
    hapus_reward,
    tukar_reward
)

from points import lihat_poin
from streak import lihat_streak

# Tugas 12
from export_json import export_data
from import_json import import_data
from laporan import laporan_streakly

while True:

    print("\n========== STREAKLY ==========")
    print("Selamat datang di Streakly! We are happy to assist you to reach your goals!")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Selesaikan Tugas")
    print("4. Hapus Tugas")
    print("5. Menu Reward")
    print("6. Lihat Poin")
    print("7. Lihat Streak")
    print("8. Export Data (JSON)")
    print("10. Laporan Streakly")
    print("11. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":

        tambah_tugas()

    elif pilihan == "2":

        lihat_tugas()

    elif pilihan == "3":

        selesaikan_tugas()

    elif pilihan == "4":

        hapus_tugas()

    elif pilihan == "5":

        while True:

            print("\n===== MENU REWARD =====")
            print("1. Tambah Reward")
            print("2. Lihat Reward")
            print("3. Edit Reward")
            print("4. Hapus Reward")
            print("5. Tukar Reward")
            print("6. Kembali")

            pilih_reward = input("Pilih menu reward : ")

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

    elif pilihan == "6":

        lihat_poin()

    elif pilihan == "7":

        lihat_streak()

    elif pilihan == "8":

        export_data()

    elif pilihan == "9":

        import_data()

    elif pilihan == "10":
        laporan_streakly()
    
    elif pilihan == "11":
        print("Terima kasih telah menggunakan Streakly.")
    break