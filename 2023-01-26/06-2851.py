lst = [int(input()) for _ in range(10)]

sum_lst = [0 for _ in range(10)]
sum_lst[0] = lst[0]

for i in range(1,10):
    sum_lst[i] = sum_lst[i-1] + lst[i]

near_100 = []
for x in sum_lst:
    near_100.append(abs(x - 100))

min_value = min(near_100)
if near_100.count(min_value) == 2:
    idx = near_100.index(min_value) + 1

else:
    idx = near_100.index(min_value)

answer = sum_lst[idx]

print(answer)
