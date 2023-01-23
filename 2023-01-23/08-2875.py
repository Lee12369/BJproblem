N, M, K = map(int, input().split())

max_team = []

for num in range(K + 1):
    able_team = min((N - num) // 2, M -K + num)
    max_team.append(able_team)

answer = max(max_team)

print(answer)
