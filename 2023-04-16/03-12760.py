import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr_nums = [sorted(list(map(int, input().split())), reverse=True) for _ in range(N)]

scores = [0 for _ in range(N)]
for j in range(M):
    winner = []
    max_num = 0
    for i in range(N):
        if arr_nums[i][j] > max_num:
            max_num = arr_nums[i][j]
            winner = [i]
        
        elif arr_nums[i][j] == max_num:
            winner.append(i)

    for idx in winner:
        scores[idx] += 1

max_score = max(scores)
for i in range(N):
    if scores[i] == max_score:
        print(i + 1, end=' ')