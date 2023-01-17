import math
N = input()
N_list = list(map(int, N))
zero_to_nine = [i for i in range(10)]
count_list = [0 for _ in range(10)]

for i in zero_to_nine:
    cnt = 0
    for j in N_list:
        if i == j:
            cnt +=1
    count_list[i] = cnt

count_list[6] = math.ceil((count_list[6] + count_list[9]) / 2)
del count_list[9]

answer = max(count_list)

print(answer)