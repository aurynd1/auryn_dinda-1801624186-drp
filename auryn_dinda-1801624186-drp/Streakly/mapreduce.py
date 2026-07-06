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

    cursor.execute("""
        SELECT *
        FROM task
    """)

    data["task"] = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM reward
    """)

    data["reward"] = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM point
    """)

    data["point"] = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM streak
    """)

    data["streak"] = cursor.fetchall()

    cursor.execute("""
        SELECT *
        FROM penukaran_reward
    """)

    data["penukaran_reward"] = cursor.fetchall()

    return data


# =========================
# MAP PHASE
# =========================
def map_task(task_data):

    hasil_map = []

    for task in task_data:

        status = task[2]

        hasil_map.append((status, 1))

    return hasil_map


# =========================
# SHUFFLE PHASE
# =========================
def shuffle_task(mapped_data):

    hasil_shuffle = {}

    for status, nilai in mapped_data:

        if status not in hasil_shuffle:

            hasil_shuffle[status] = []

        hasil_shuffle[status].append(nilai)

    return hasil_shuffle


# =========================
# FILTER PHASE
# =========================
def filter_task(shuffled_data):

    hasil_filter = {}

    for status, daftar in shuffled_data.items():

        if len(daftar) > 0:

            hasil_filter[status] = daftar

    return hasil_filter


# =========================
# REDUCE PHASE
# =========================
def reduce_task(filtered_data):

    hasil_reduce = {}

    for status, daftar in filtered_data.items():

        hasil_reduce[status] = sum(daftar)

    return hasil_reduce


# =========================
# MAP PHASE (REWARD)
# =========================
def map_reward(reward_data):

    hasil_map = []

    for reward in reward_data:

        status = reward[3]

        hasil_map.append((status, 1))

    return hasil_map


    # =========================
# SHUFFLE PHASE (REWARD)
# =========================
def shuffle_reward(mapped_data):

    hasil_shuffle = {}

    for status, nilai in mapped_data:

        if status not in hasil_shuffle:

            hasil_shuffle[status] = []

        hasil_shuffle[status].append(nilai)

    return hasil_shuffle


    # =========================
# FILTER PHASE (REWARD)
# =========================
def filter_reward(shuffled_data):

    hasil_filter = {}

    for status, daftar in shuffled_data.items():

        if len(daftar) > 0:

            hasil_filter[status] = daftar

    return hasil_filter


    # =========================
# REDUCE PHASE (REWARD)
# =========================
def reduce_reward(filtered_data):

    hasil_reduce = {}

    for status, daftar in filtered_data.items():

        hasil_reduce[status] = sum(daftar)

    return hasil_reduce


    # =========================
# MAP PHASE (POINT)
# =========================
def map_point(point_data):

    hasil_map = []

    for point in point_data:

        hasil_map.append(point[0])

    return hasil_map


    # =========================
# REDUCE PHASE (POINT)
# =========================
def reduce_point(mapped_data):

    return sum(mapped_data)


# =========================
# MAIN PROGRAM
# =========================
def analisis_streakly():

    data = ambil_data()

    print("\n========== ANALISIS STREAKLY ==========")

    # =========================
    # TASK
    # =========================
    hasil_map = map_task(data["task"])

    hasil_shuffle = shuffle_task(hasil_map)

    hasil_filter = filter_task(hasil_shuffle)

    hasil_reduce = reduce_task(hasil_filter)

    print("\n[TASK]")

    total = sum(hasil_reduce.values())

    selesai = hasil_reduce.get("Selesai", 0)

    belum = hasil_reduce.get("Belum Selesai", 0)

    print(f"Total Task : {total}")
    print(f"Task Selesai : {selesai}")
    print(f"Task Belum Selesai : {belum}")

    if total != 0:

        persen = (selesai / total) * 100

        print(f"Persentase Penyelesaian : {persen:.2f}%")

    else:

        print("Persentase Penyelesaian : 0%")

    # =========================
    # BAGIAN ANGGOTA
    # =========================
 # =========================
# REWARD
# =========================
hasil_map = map_reward(data["reward"])

hasil_shuffle = shuffle_reward(hasil_map)

hasil_filter = filter_reward(hasil_shuffle)

hasil_reduce = reduce_reward(hasil_filter)

print("\n[REWARD]")

total_reward = sum(hasil_reduce.values())

ditukar = hasil_reduce.get("Ditukar", 0)

belum = hasil_reduce.get("Belum Ditukar", 0)

print(f"Total Reward : {total_reward}")
print(f"Reward Ditukar : {ditukar}")
print(f"Reward Belum Ditukar : {belum}")

# =========================
# POINT
# =========================
hasil_point = reduce_point(
    map_point(data["point"])
)

print("\n[POINT]")
print(f"Total Poin : {hasil_point}")

    print("\n[STREAK]")
    print("Dikerjakan Cintia")

    print("\n[PENUKARAN REWARD]")
    print("Dikerjakan Cintia")


# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":

    analisis_streakly()

    conn.close()
