from collections import defaultdict
N = [int(input()) for _ in range(10)]

average = int(sum(N) / 10)

dic = defaultdict(int)

for x in N:
    dic[x] += 1

max_val = max(dic.values())

for key, val in dic.items():
    if val == max_val:
        mode = key

print(average)
print(mode)