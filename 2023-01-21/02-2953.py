sum_list = []

for i in range(5):
    numbers = map(int,input().split())
    sum_list.append(sum(numbers))

max_val = max(sum_list)
max_index = sum_list.index(max_val)

print(max_index + 1)
print(max_val)

