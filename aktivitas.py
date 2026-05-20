from datetime import datetime

# =====================================================
# PROGRAM MANAJEMEN AKTIVITAS
# =====================================================

print("=" * 50)
print("      PROGRAM MANAJEMEN AKTIVITAS")
print("=" * 50)

# Input aktivitas
aktivitas = input(
    "\nMasukkan aktivitas (sarapan/kerja): "
).lower()

# =====================================================
# AKTIVITAS SARAPAN
# =====================================================

if aktivitas == "sarapan":

    print("\n===== MENU SARAPAN =====")
    print("- telur")
    print("- ikan")
    print("- nugget")
    print("- roti")
    print("- sereal")

    # Input menu sarapan
    menu = input(
        "\nMasukkan menu sarapan yang diinginkan: "
    ).lower()

    # Daftar bahan tersedia
    bahan_tersedia = [
        "telur",
        "ikan",
        "nugget",
        "roti",
        "sereal"
    ]

    # Cek bahan tersedia
    if menu in bahan_tersedia:

        print(f"\nBahan {menu} tersedia di lokasi Anda.")

        # Cek ingin masak atau tidak
        masak = input(
            f"Apakah Anda ingin memasak {menu}? (ya/tidak): "
        ).lower()

        if masak == "ya":

            print(f"\nSedang menyiapkan {menu}...")

            # Estimasi waktu memasak
            if menu == "telur":
                print("Estimasi memasak: 5 menit")

            elif menu == "ikan":
                print("Estimasi memasak: 15 menit")

            elif menu == "nugget":
                print("Estimasi memasak: 10 menit")

            elif menu == "roti":
                print("Estimasi menyiapkan: 3 menit")

            elif menu == "sereal":
                print("Estimasi menyiapkan: 2 menit")

            print(f"{menu.capitalize()} berhasil disiapkan.")
            print("Selamat menikmati sarapan Anda!")

        else:
            print("\nAnda memilih tidak memasak.")
            print("Sarapan dibatalkan.")

    else:
        print(f"\nBahan untuk menu {menu} tidak tersedia.")
        print("Silakan membeli bahan terlebih dahulu.")

# =====================================================
# AKTIVITAS KERJA
# =====================================================

elif aktivitas == "kerja":

    waktu_sekarang = datetime.now()

    jam = waktu_sekarang.hour
    menit = waktu_sekarang.minute

    print("\n===== STATUS KERJA =====")
    print("Waktu sekarang:", jam, ":", menit)

    # Cek keterlambatan
    if jam > 8 or (jam == 8 and menit > 0):

        print("Anda terlambat masuk kerja")

        # Hitung total keterlambatan
        telat_menit = ((jam - 8) * 60) + menit

        print("Total keterlambatan:",
              telat_menit, "menit")

        # Notifikasi tambahan
        if telat_menit <= 15:
            print("Segera masuk dan mulai bekerja.")
        else:
            print("Anda mendapat peringatan keterlambatan.")

    else:

        print("Anda belum terlambat masuk kerja")
        print("Semangat bekerja hari ini!")

        # Hitung sisa waktu sebelum jam kerja
        sisa_waktu = ((8 - jam) * 60) - menit

        print("Sisa waktu sebelum jam kerja:",
              sisa_waktu, "menit")

    # Cek mood kerja
    mood = input(
        "\nBagaimana mood Anda hari ini? "
        "(semangat/capek/biasa): "
    ).lower()

    if mood == "semangat":
        print("Pertahankan semangat kerja Anda!")

    elif mood == "capek":
        print("Jangan lupa istirahat sejenak.")

    else:
        print("Semoga hari kerja Anda menyenangkan.")

# =====================================================
# JIKA AKTIVITAS TIDAK TERSEDIA
# =====================================================

else:
    print("\nAktivitas tidak tersedia.")

# =====================================================
# PENUTUP
# =====================================================

print("\nTerima kasih telah menggunakan program.")
