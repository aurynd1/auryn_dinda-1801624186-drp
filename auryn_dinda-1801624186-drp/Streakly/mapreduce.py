import sqlite3

# =========================
# KONEKSI DATABASE
# =========================
conn = sqlite3.connect("streakly.db")
cursor = conn.cursor()


# =========================
# AMBIL DATA DATABASE
# =========================
def ambil_data():

    data = {}

    cursor.execute("SELECT * FROM task")
    data["task"] = cursor.fetchall()

    cursor.execute("SELECT * FROM reward")
    data["reward"] = cursor.fetchall()

    cursor.execute("SELECT * FROM point")
    data["point"] = cursor.fetchall()

    cursor.execute("SELECT * FROM streak")
    data["streak"] = cursor.fetchall()

    cursor.execute("SELECT * FROM penukaran_reward")
    data["penukaran_reward"] = cursor.fetchall()

    return data


# ======================================================
# TASK
# ======================================================
def map_task(task_data):

    hasil_map = []

    for task in task_data:
        hasil_map.append((task[2], 1))

    return hasil_map


def shuffle_task(mapped_data):

    hasil_shuffle = {}

    for status, nilai in mapped_data:

        if status not in hasil_shuffle:
            hasil_shuffle[status] = []

        hasil_shuffle[status].append(nilai)

    return hasil_shuffle


def filter_task(shuffled_data):

    hasil_filter = {}

    for status, daftar in shuffled_data.items():

        if len(daftar) > 0:
            hasil_filter[status] = daftar

    return hasil_filter


def reduce_task(filtered_data):

    hasil_reduce = {}

    for status, daftar in filtered_data.items():
        hasil_reduce[status] = sum(daftar)

    return hasil_reduce


# ======================================================
# REWARD
# ======================================================
def map_reward(reward_data):

    hasil_map = []

    for reward in reward_data:
        hasil_map.append((reward[3], 1))

    return hasil_map


def shuffle_reward(mapped_data):

    hasil_shuffle = {}

    for status, nilai in mapped_data:

        if status not in hasil_shuffle:
            hasil_shuffle[status] = []

        hasil_shuffle[status].append(nilai)

    return hasil_shuffle


def filter_reward(shuffled_data):

    hasil_filter = {}

    for status, daftar in shuffled_data.items():

        if len(daftar) > 0:
            hasil_filter[status] = daftar

    return hasil_filter


def reduce_reward(filtered_data):

    hasil_reduce = {}

    for status, daftar in filtered_data.items():
        hasil_reduce[status] = sum(daftar)

    return hasil_reduce


# ======================================================
# POINT
# ======================================================
def map_point(point_data):

    hasil_map = []

    for point in point_data:
        hasil_map.append(point[0])

    return hasil_map


def reduce_point(mapped_data):

    return sum(mapped_data)


# ======================================================
# STREAK
# ======================================================
def map_streak(streak_data):

    hasil_map = []

    for streak in streak_data:
        hasil_map.append(streak[0])

    return hasil_map


def reduce_streak(mapped_data):

    if len(mapped_data) == 0:
        return 0

    return mapped_data[0]


# ======================================================
# PENUKARAN REWARD
# ======================================================
def map_penukaran(data_penukaran):

    hasil_map = []

    for item in data_penukaran:
        hasil_map.append((item[1], 1))

    return hasil_map


def shuffle_penukaran(mapped_data):

    hasil_shuffle = {}

    for reward, nilai in mapped_data:

        if reward not in hasil_shuffle:
            hasil_shuffle[reward] = []

        hasil_shuffle[reward].append(nilai)

    return hasil_shuffle


def filter_penukaran(shuffled_data):

    hasil_filter = {}

    for reward, daftar in shuffled_data.items():

        if len(daftar) > 0:
            hasil_filter[reward] = daftar

    return hasil_filter


def reduce_penukaran(filtered_data):

    hasil_reduce = {}

    for reward, daftar in filtered_data.items():
        hasil_reduce[reward] = sum(daftar)

    return hasil_reduce


# ======================================================
# MAIN PROGRAM
# ======================================================
def analisis_streakly():

    data = ambil_data()

    print("\n========== ANALISIS STREAKLY ==========")

    # -------------------------
    # TASK
    # -------------------------
    hasil_map = map_task(data["task"])
    hasil_shuffle = shuffle_task(hasil_map)
    hasil_filter = filter_task(hasil_shuffle)
    hasil_reduce = reduce_task(hasil_filter)

    print("\n[TASK]")

    total_task = sum(hasil_reduce.values())
    selesai = hasil_reduce.get("Selesai", 0)
    belum = hasil_reduce.get("Belum Selesai", 0)

    print(f"Total Task              : {total_task}")
    print(f"Task Selesai            : {selesai}")
    print(f"Task Belum Selesai      : {belum}")

    if total_task != 0:
        persen = (selesai / total_task) * 100
    else:
        persen = 0

    print(f"Persentase Penyelesaian : {persen:.2f}%")

    # -------------------------
    # REWARD
    # -------------------------
    hasil_map = map_reward(data["reward"])
    hasil_shuffle = shuffle_reward(hasil_map)
    hasil_filter = filter_reward(hasil_shuffle)
    hasil_reduce = reduce_reward(hasil_filter)

    print("\n[REWARD]")

    total_reward = sum(hasil_reduce.values())
    ditukar = hasil_reduce.get("Ditukar", 0)
    belum = hasil_reduce.get("Belum Ditukar", 0)

    print(f"Total Reward        : {total_reward}")
    print(f"Reward Ditukar      : {ditukar}")
    print(f"Reward Belum Ditukar: {belum}")

    # -------------------------
    # POINT
    # -------------------------
    total_point = reduce_point(map_point(data["point"]))

    print("\n[POINT]")
    print(f"Total Poin : {total_point}")

    # -------------------------
    # STREAK
    # -------------------------
    total_streak = reduce_streak(map_streak(data["streak"]))

    print("\n[STREAK]")
    print(f"Jumlah Streak : {total_streak} hari")

    # -------------------------
    # PENUKARAN REWARD
    # -------------------------
    hasil_map = map_penukaran(data["penukaran_reward"])
    hasil_shuffle = shuffle_penukaran(hasil_map)
    hasil_filter = filter_penukaran(hasil_shuffle)
    hasil_reduce = reduce_penukaran(hasil_filter)

    print("\n[PENUKARAN REWARD]")

    if len(hasil_reduce) == 0:
        print("Belum ada penukaran reward.")
    else:
        for reward, jumlah in hasil_reduce.items():
            print(f"{reward} : {jumlah} kali")


# ======================================================
# RUN PROGRAM
# ======================================================
if __name__ == "__main__":

    analisis_streakly()

    conn.close()