cost_1, cost_2, cost_3 = map(int, input().split())

numbers = []
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        numbers.append(i)

min_num = min(numbers)
max_num = max(numbers)
total_cost = 0
for i in range(min_num, max_num + 1):
    cnt = numbers.count(i)
    if cnt == 1:
        total_cost += cnt * cost_1
    elif cnt == 2:
        total_cost += cnt * cost_2
    elif cnt == 3:
        total_cost += cnt * cost_3    

print(total_cost)