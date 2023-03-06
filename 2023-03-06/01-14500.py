import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def I4_shape():
    # 가로 
    max_score = 0
    for i in range(N):
        for j in range(M - 3):
            score = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3]
            max_score = max(max_score, score)
    # 세로
    for i in range(N - 3):
        for j in range(M):
            score = arr[i][j] + arr[i + 1][j] + arr[i + 2][j] + arr[i + 3][j]
            max_score = max(max_score, score)
    
    return max_score

def box_shape():
    max_score = 0
    for i in range(N - 1):
        for j in range(M - 1):
            score = arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            max_score = max(max_score, score)

    return max_score

def I3_shape():
    # 연속으로 3개의 값을 기준으로 주위값을 처리. 결과적으로 L 모양과 ㅜ 모양을 처리할 수 있다.
    max_score = 0
    #가로
    dx = [-1, -1, -1, 1, 1, 1]
    dy = [0, 1, 2, 0, 1, 2]
    for i in range(N):
        for j in range(M - 2):
            score = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            max_num = 0
            for k in range(6):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    max_num = max(max_num, arr[ni][nj])
            score += max_num
            max_score = max(max_score, score)
    
    #세로
    dx = [0, 1, 2, 0, 1, 2]
    dy = [-1, -1, -1, 1, 1, 1]
    for i in range(N - 2):
        for j in range(M):
            score = arr[i][j] + arr[i + 1][j] + arr[i + 2][j]
            max_num = 0
            for k in range(6):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    max_num = max(max_num, arr[ni][nj])
            score += max_num
            max_score = max(max_score, score)
    
    return max_score

def I2_shape():
    # ㄹ 모양을 확인.
    max_score = 0

    # 가로 - 역가로
    for i in range(N - 1):
        for j in range(M - 2):
            # 가로
            score_1 = arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1] + arr[i + 1][j + 2]
            # 역가로
            score_2 = arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j] + arr[i + 1][j + 1]
            max_score = max(max_score, score_1, score_2)
    
    # 세로 - 역세로
    for i in range(N - 2):
        for j in range(M - 1):
            # 세로
            score_1 = arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j + 1]
            # 역세로
            score_2 = arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1] + arr[i + 2][j]
            max_score = max(max_score, score_1, score_2)
    
    return max_score

ans = max(I2_shape(), I3_shape(), I4_shape(), box_shape())

print(ans)