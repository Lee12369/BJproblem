import sys, copy
input = sys.stdin.readline

# CCTV 번호 별로 각 인덱스 별로 하나의 case를 저장
def CCTV1():
    dx = [[0], [0], [1], [-1]]
    dy = [[1], [-1], [0], [0]]
    return dx, dy

def CCTV2():
    dx = [[0, 0], [1, -1]]
    dy = [[1, -1], [0, 0]]
    return dx, dy

def CCTV3():
    dx = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    dy = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    return dx, dy

def CCTV4():
    dx = [[0, 0, 1], [0, 0, -1], [0, 1, -1], [0, 1, -1]]
    dy = [[1, -1, 0], [1, -1, 0], [1, 0, 0], [-1, 0, 0],]
    return dx, dy

def CCTV5():
    dx = [[0, 0, 1, -1]]
    dy = [[1, -1, 0, 0]]
    return dx, dy

def back_tracking(board, visited, cctv):
    for num, lst in enumerate(cctv):
        for tpl in lst:
            i, j = tpl
            if visited[(i, j)] == False:
                visited[(i, j)] = True
                # cctv 변호가 적힌 CCTV함수에 담긴 dx, dy를 얻는다.
                dx, dy = cctv_dic[num]()

                return watch(board, i, j, dx, dy, visited, cctv)

    # cctv 전부를 설치한 경우 사각지대 개수 저장 
    cnt_0 = 0
    for lst in board:
        cnt_0 += lst.count(0)
    answer.append(cnt_0)

# cctv : 번호에 따라 위치를 저장, visited : 위치에 있는 cctv 방문 여부를 확인
def get_cctv():
    visited = {}
    cctv = [[] for _ in range(6)]
    for i in range(N):
        for j in range(M):
            cctv_num = board[i][j]
            if  cctv_num == 6 or cctv_num == 0:
                continue
            
            cctv[cctv_num].append((i, j))
            visited[(i, j)] = False

    return cctv, visited

def watch(board, x, y, dx, dy, visited, cctv):
    for i in range(len(dx)):
        ## copy를 하지 않으면 다른 분기점에서 영향을 주기에 다시 백트래킹을 하기 전에 미리 새로운 board, visited를 만들어야 한다.
        save_board = copy.deepcopy(board)
        save_visited = copy.deepcopy(visited)
        for j in range(len(dx[i])):
            save_x = int(x)
            save_y = int(y)
            while True:
                nx = save_x + dx[i][j]
                ny = save_y + dy[i][j]
                if 0 <= nx < N and 0 <= ny < M:
                    if save_board[nx][ny] == 0:
                        save_board[nx][ny] = '#'
                    elif save_board[nx][ny] == 6:
                        break
                else:
                    break
                save_x = int(nx)
                save_y = int(ny)
        
        back_tracking(save_board, save_visited, cctv)


cctv_dic = {
    1 : CCTV1,
    2 : CCTV2,
    3 : CCTV3,
    4 : CCTV4,
    5 : CCTV5,
}

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = []
cctv, visited = get_cctv()

back_tracking(board, visited, cctv)

ans = min(answer)

print(ans)
