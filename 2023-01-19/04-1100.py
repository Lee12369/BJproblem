lst = [list(str(input())) for _ in range(8)]
white_place = []


for i in range(0, 8, 2):
    for j in range(0, 8, 2):
        white_place.append(lst[i][j])

for i in range(1, 8, 2):
    for j in range(1, 8, 2):
        white_place.append(lst[i][j])

answer = white_place.count('F')

print(answer)