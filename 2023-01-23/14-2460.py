lst = [list(map(int, input().split())) for _ in range(10)]

riding_N = [lst[0][1]]

for i in range(1,10):
    num = riding_N[i-1] + lst[i][1] - lst[i][0]
    riding_N.append(num)

answer = max(riding_N)

print(answer)