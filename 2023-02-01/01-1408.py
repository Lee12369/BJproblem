start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

answer = [0 for _ in range(3)]

for i in range(2,-1,-1):
    answer[i] = end[i] - start[i]
    if answer[0] < 0:
        answer[0] += 24

    elif answer[i] < 0:
        end[i-1] -= 1
        answer[i] += 60

for i in range(3):
    if answer[i] < 10:
        answer[i] = '0' + str(answer[i])

print("{}:{}:{}".format(answer[0], answer[1], answer[2]))
