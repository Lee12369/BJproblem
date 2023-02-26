N = int(input())
lost_HP = list(map(int, input().split())) 
get_joy = list(map(int, input().split())) 


dp_HP = [[] for _ in range(N + 1)]
dp_joy = [[] for _ in range(N + 1)]

dp_HP[0] = [100]
dp_joy[0] = [0]

for i in range(1, N + 1):
    dp_HP[i] = dp_HP[i - 1]
    dp_joy[i] = dp_joy[i - 1]
    M = len(dp_HP[i - 1])
    for j in range(M):
        if dp_HP[i - 1][j] - lost_HP[i - 1] > 0:
            HP = dp_HP[i - 1][j] - lost_HP[i - 1]
            joy = dp_joy[i - 1][j] + get_joy[i - 1]
            dp_HP[i].append(HP)
            dp_joy[i].append(joy)

ans = max(dp_joy[N])

print(ans)
