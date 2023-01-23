arr = [list(map(int, input().split())) for _ in range(9)]

numbers = []

for i in range(9):
    numbers.append(max(arr[i]))

max_number = max(numbers)

maxi_index = numbers.index(max_number)
maxj_index = arr[maxi_index].index(max_number)

print(max_number)
print("{} {}".format(maxi_index + 1, maxj_index + 1))