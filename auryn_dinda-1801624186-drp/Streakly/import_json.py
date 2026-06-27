import sqlite3
import json

conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


def import_data():

    try:

        with open("backup_streakly.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        print("File backup_streakly.json tidak ditemukan.")
        return

    # =========================
    # Hapus data lama
    # =========================
    cursor.execute("DELETE FROM task")
    cursor.execute("DELETE FROM reward")
    cursor.execute("DELETE FROM point")
    cursor.execute("DELETE FROM streak")
    cursor.execute("DELETE FROM penukaran_reward")

    # =========================
    # Import Task
    # =========================
    for task in data["task"]:

        cursor.execute("""
            INSERT INTO task
            VALUES (?, ?, ?, ?)
        """, task)

    # =========================
    # Import Reward
    # =========================
    for reward in data["reward"]:

        cursor.execute("""
            INSERT INTO reward
            VALUES (?, ?, ?, ?, ?)
        """, reward)

    # =========================
    # Import Point
    # =========================
    for point in data["point"]:

        cursor.execute("""
            INSERT INTO point
            VALUES (?)
        """, point)

    # =========================
    # Import Streak
    # =========================
    for streak in data["streak"]:

        cursor.execute("""
            INSERT INTO streak
            VALUES (?, ?)
        """, streak)

    # =========================
    # Import Riwayat Reward
    # =========================
    for penukaran in data["penukaran_reward"]:

        cursor.execute("""
            INSERT INTO penukaran_reward
            VALUES (?, ?, ?, ?)
        """, penukaran)

    conn.commit()

    print("\nData berhasil diimport dari backup_streakly.json")