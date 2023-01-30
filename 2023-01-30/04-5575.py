for _ in range(3):
    time = list(map(int, input().split()))
    time_sec = []
    for i in range(2):
        sec = time[i * 3] * 3600 + time[i * 3 + 1] * 60 + time[i * 3 + 2]
        time_sec.append(sec)

    work_time = time_sec[1] - time_sec[0]
    work_time_hour = work_time // 3600
    work_time_min = (work_time % 3600) // 60
    work_time_sec = (work_time % 3600) % 60

    print(work_time_hour, work_time_min, work_time_sec)
