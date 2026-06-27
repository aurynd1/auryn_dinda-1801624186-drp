import sqlite3
import json

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


def export_data():

    data = {}

    # =========================
    # Export Task
    # =========================
    cursor.execute("""
        SELECT *
        FROM task
    """)

    task = cursor.fetchall()

    data["task"] = task

    # =========================
    # Export Reward
    # =========================
    cursor.execute("""
        SELECT *
        FROM reward
    """)

    reward = cursor.fetchall()

    data["reward"] = reward

    # =========================
    # Export Point
    # =========================
    cursor.execute("""
        SELECT *
        FROM point
    """)

    point = cursor.fetchall()

    data["point"] = point

    # =========================
    # Export Streak
    # =========================
    cursor.execute("""
        SELECT *
        FROM streak
    """)

    streak = cursor.fetchall()

    data["streak"] = streak

    # =========================
    # Export Penukaran Reward
    # =========================
    cursor.execute("""
        SELECT *
        FROM penukaran_reward
    """)

    penukaran = cursor.fetchall()

    data["penukaran_reward"] = penukaran

    # =========================
    # Simpan ke JSON
    # =========================
    with open("backup_streakly.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print("\nData berhasil diexport ke backup_streakly.json")