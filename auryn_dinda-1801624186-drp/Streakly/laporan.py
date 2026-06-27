import sqlite3

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


def laporan_streakly():

    print("\n========== LAPORAN STREAKLY ==========")

    # =========================
    # Total Task
    # =========================
    cursor.execute("""
        SELECT COUNT(*)
        FROM task
    """)

    total_task = cursor.fetchone()[0]

    # =========================
    # Task Selesai
    # =========================
    cursor.execute("""
        SELECT COUNT(*)
        FROM task
        WHERE status='Selesai'
    """)

    task_selesai = cursor.fetchone()[0]

    # =========================
    # Task Belum Selesai
    # =========================
    cursor.execute("""
        SELECT COUNT(*)
        FROM task
        WHERE status='Belum Selesai'
    """)

    task_belum = cursor.fetchone()[0]

    # =========================
    # Persentase
    # =========================
    if total_task == 0:
        persentase = 0
    else:
        persentase = (task_selesai / total_task) * 100

    print(f"Total Task              : {total_task}")
    print(f"Task Selesai            : {task_selesai}")
    print(f"Task Belum Selesai      : {task_belum}")
    print(f"Persentase Penyelesaian : {persentase:.2f}%")
        print("\n========== PROGRESS USER ==========")

    # =========================
    # Total Reward
    # =========================
    cursor.execute("""
        SELECT COUNT(*)
        FROM reward
    """)

    total_reward = cursor.fetchone()[0]

    # =========================
    # Reward Ditukar
    # =========================
    cursor.execute("""
        SELECT COUNT(*)
        FROM penukaran_reward
    """)

    reward_ditukar = cursor.fetchone()[0]

    # =========================
    # Total Poin
    # =========================
    cursor.execute("""
        SELECT jumlah_poin
        FROM point
    """)

    hasil = cursor.fetchone()

    if hasil:
        total_poin = hasil[0]
    else:
        total_poin = 0

    # =========================
    # Current Streak
    # =========================
    cursor.execute("""
        SELECT jumlah_hari
        FROM streak
    """)

    hasil = cursor.fetchone()

    if hasil:
        streak = hasil[0]
    else:
        streak = 0

    print(f"Jumlah Reward      : {total_reward}")
    print(f"Reward Ditukar     : {reward_ditukar}")
    print(f"Total Poin         : {total_poin}")
    print(f"Current Streak     : {streak} hari")