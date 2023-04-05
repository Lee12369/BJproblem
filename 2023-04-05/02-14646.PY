N = int(input())
nums = list(map(int, input().split()))

visited = [0 for _ in range(N + 1)]
cnt = 0
max_sticker_cnt = 0
for x in nums:
    if visited[x] == 0:
        visited[x] = 1
        cnt += 1
        max_sticker_cnt = max(max_sticker_cnt, cnt)

    elif visited[x] == 1:
        visited[x] == 0
        cnt -= 1

print(max_sticker_cnt)

