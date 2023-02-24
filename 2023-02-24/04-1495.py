from collections import deque
N, S, M = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque()
queue.append(S)

dx = [1, -1]
for i in range(1, N + 1):
    dp = set()
    while queue:
        x = queue.popleft()
        for j in range(2):
            temp = x + nums[i - 1] * dx[j]
            if 0 <= temp <= M:
                dp.add(temp)
    queue.extend(dp)

if dp:
    ans = max(dp)
else:
    ans = -1

print(ans)
