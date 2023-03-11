import sys
input = sys.stdin.readline

N = int(input())

dic = {}
for _ in range(N * N):
    key, val1, val2, val3, val4 = map(int, input().split())
    dic[key] = [val1, val2, val3, val4]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = [[0 for _ in range(N)] for _ in range(N)]
for key in dic.keys():
    cnd = []
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            rule1_cnt = 0
            rule2_cnt = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] in dic[key]:
                        rule1_cnt += 1
                    if arr[ni][nj] == 0:
                        rule2_cnt += 1

            cnd.append([rule1_cnt, rule2_cnt, i, j])
    # 규칙에 따라 우선순위를 정해 정렬
    cnd.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
    
    # 우선 순위에 따라 빈 공간일 경우 위치 선정. 빈 공간이 아니면 다음 순위로 넘어감.
    for lst in cnd:
        if arr[lst[2]][lst[3]] == 0:
            arr[lst[2]][lst[3]] = key
            break

# 만족도
satisfy = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] in dic[arr[i][j]]:
                    cnt += 1
        if cnt > 0:
            satisfy += 10 ** (cnt - 1)

print(satisfy)