import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input()) for _ in range(N)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

ans_arr = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == '.':
            mine_cnt = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] != '.':
                        mine_cnt += int(arr[nx][ny])
            if mine_cnt >= 10:
                mine_cnt = 'M'
            ans_arr[i][j] = mine_cnt
        
        else:
            ans_arr[i][j] = '*'

for lst in ans_arr:
    for x in lst:
        print(x, end='')
    print()