# 포기, 시간 초과
import sys
row, column, add_block = map(int, sys.stdin.readline().split())

numbers = []
for i in range(row):
    numbers += map(int, sys.stdin.readline().split())

max_num = max(numbers)
min_num = min(numbers)
N = len(numbers)

time_lst = []
height_lst = []
for height in range(max_num, min_num-1, -1):
    time = 0
    bag = add_block
    for i in range(N):
        if numbers[i] > height:
            time += (numbers[i] - height) * 2
            bag += numbers[i] - height
        
        else:
            time += height - numbers[i]
            bag -= height - numbers[i]
            
    if bag >= 0:
        time_lst.append(time)
        height_lst.append(height)

min_time = min(time_lst)
idx = time_lst.index(min_time)
height = height_lst[idx]

print(min_time, height)