N = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]

max_value = lst[0][1]
max_index = 0
for i in range(6):
    if lst[i][1] >= max_value:
        max_value = lst[i][1]
        max_index = i

if max_index >= 4:
    max_index -= 6
elif max_index <= -4:
    max_index += 6

width = [max_value]
height = [lst[max_index - 1][1], lst[max_index + 1][1]]


if lst[max_index - 1][1] > lst[max_index + 1][1]:
    width.append(lst[max_index - 2][1])
else:
    width.append(lst[max_index + 2][1])

square = (max(width) * max(height)) - (max(width) - min(width))*(max(height) - min(height))
answer = square * N

print(answer)