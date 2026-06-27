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