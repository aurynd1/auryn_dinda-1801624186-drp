
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
from export_json import export_data
from import_json import import_data
from laporan import laporan_streakly

while True:

    print("\n========== STREAKLY ==========")
    print("Selamat datang di Streakly! We are happy to assist you to reach your goals!")
    print("1. Task📋") 
    print("2. Reward🎁")
    print("3. Point⭐")
    print("4. Streak🔥")
    print("5. Laporan📈")
    print("6. Tools🛠️")
    print("7. Keluar🔚")

    pilihan = input("Pilih menu : ")

    # ==================================================
    # MENU TASK
    # ==================================================
    if pilihan == "1":

        while True:

            print("\n===== MENU TASK =====")
            print("1. Tambah Tugas")
            print("2. Lihat Tugas")
            print("3. Selesaikan Tugas")
            print("4. Hapus Tugas")
            print("5. Kembali")

            pilih_task = input("Pilih menu task : ")

            if pilih_task == "1":

                tambah_tugas()

            elif pilih_task == "2":

                lihat_tugas()

            elif pilih_task == "3":

                selesaikan_tugas()

            elif pilih_task == "4":

                hapus_tugas()

            elif pilih_task == "5":

                break

            else:

                print("Pilihan tidak tersedia.")

    # ==================================================
    # MENU REWARD
    # ==================================================
    elif pilihan == "2":

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

    # ==================================================
    # MENU POINT
    # ==================================================
    elif pilihan == "3":

        while True:

            print("\n===== MENU POINT =====")
            print("1. Lihat Poin")
            print("2. Kembali")

            pilih_point = input("Pilih menu point : ")

            if pilih_point == "1":

                lihat_poin()

            elif pilih_point == "2":

                break

            else:

                print("Pilihan tidak tersedia.")

    # ==================================================
    # MENU STREAK
    # ==================================================
    elif pilihan == "4":

        while True:

            print("\n===== MENU STREAK =====")
            print("1. Lihat Streak")
            print("2. Kembali")

            pilih_streak = input("Pilih menu streak : ")

            if pilih_streak == "1":

                lihat_streak()

            elif pilih_streak == "2":

                break

            else:

                print("Pilihan tidak tersedia.")

    # ==================================================
    # MENU LAPORAN
    # ==================================================
    elif pilihan == "5":

        while True:

            print("\n===== MENU LAPORAN =====")
            print("1. Tampilkan Laporan")
            print("2. Kembali")

            pilih_laporan = input("Pilih menu laporan : ")

            if pilih_laporan == "1":

                laporan_streakly()

            elif pilih_laporan == "2":

                break

            else:

                print("Pilihan tidak tersedia.")

    # ==================================================
    # MENU TOOLS
    # ==================================================
    elif pilihan == "6":

        while True:

            print("\n===== MENU TOOLS =====")
            print("1. Export Data (JSON)")
            print("2. Import Data (JSON)")
            # print("3. Analisis MapReduce")
            print("3. Kembali")

            pilih_tools = input("Pilih menu tools : ")

            if pilih_tools == "1":

                export_data()

            elif pilih_tools == "2":

                import_data()

            # elif pilih_tools == "3":
            #
            #     analisis_streakly()

            elif pilih_tools == "3":

                break

            else:

                print("Pilihan tidak tersedia.")

    # ==================================================
    # KELUAR
    # ==================================================
    elif pilihan == "7":

        print("\nTerima kasih telah menggunakan Streakly.")
        break

    else:

        print("Pilihan tidak tersedia.")