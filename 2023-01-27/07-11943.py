lst = [list(map(int, input().split())) for i in range(2)]

N = lst[0][0] + lst[1][1]
M = lst[0][1] + lst[1][0]

answer = min(N,M)

print(answer)