import sys, copy
input = sys.stdin.readline

def back_tracking(board, start_i, cnt, visited):
    horizontal_line = cnt + M
    if horizontal_line % 2 == 0:                
        diff_cnt = check_ladder(board)
        # 다른 게 없으면 cnt 저장 후 종료
        if diff_cnt == 0:
            answer.append(cnt)
            return
        # 가로선을 하나 추가하면 2개의 수의 위치가 바뀐다. 이를 이용하여 남은 가로선의 개수를 이용하여 종료 조건 추가. ex) 남은 가로선이 2개고 서로 다른 수가 5개라면 최대로 바꿀 수 있는 수는 4개이므로 즉시 종료한다. 
        if diff_cnt > 2 * (3 - cnt):
            return
    
    if cnt == 3:
        return
    
    for i in range(start_i, H + 1):
        for j in range(1, N):
            if visited[i][j] == 0 and board[i][j] == False and board[i][j + 1] == False:
                visited[i][j] = 1
    
                new_board = copy.deepcopy(board)
                new_board[i][j] = (i, j + 1)
                new_board[i][j + 1] = (i, j)

                new_cnt = cnt + 1
          
                back_tracking(new_board, i, new_cnt, visited)

                visited[i][j] = 0
                
def check_ladder(board):
    diff_cnt = 0
    for num in range(1, N + 1):
        curr_j = int(num)
        for i in range(1, H + 1):
            if board[i][curr_j]:
                curr_j = board[i][curr_j][1]

        if not num == curr_j:
            diff_cnt += 1
            
    return diff_cnt

def save_move(board):
    # 가로선이 생기는 위치에 도착하면 이동할 위치를 tuple형태로 저장한다.
    for _ in range(M):
        a, b = map(int, input().split())
        board[a][b] = (a, b + 1)
        board[a][b + 1] = (a, b)
    return board

N, M, H = map(int, input().split())

board = [[False for _ in range(N + 1)] for _ in range(H + 1)]
board = save_move(board)

answer = []
start_i = 1
cnt = 0
visited = [[0 for _ in range(N + 1)] for _ in range(H + 1)]

back_tracking(board, start_i, cnt, visited)

if answer:
    ans = min(answer)
    print(ans)
else:
    print(-1)