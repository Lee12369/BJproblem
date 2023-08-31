from collections import deque, defaultdict
import sys
input = sys.stdin.readline

# 빌딩 안으로 들어갈 수 있는 입구를 저장. 소문자, 대문자. 빈 공간, 문서. 총 4가지 경우를 고려하여 진행.
# 열쇠 발견시 문으로 막혀 있는 부분을 열 수 있을지도 모르기에 다시 함수를 실행한다.
def into_building(board, keys, doors):
    entrances = []
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                door = board[i][j]
                if door == '.' or door == '$':    
                    entrances.append((i, j))
                    board[i][j] = '.'
                
                elif door.isupper():
                    doors[door] = True
                    if keys[door.lower()]:
                        entrances.append((i, j))
                        board[i][j] = '.'
                        del doors[door]

                elif door.islower():
                    key = door
                    keys[key] = True
                    board[i][j] = '.'
                    return into_building(board, keys, doors)
                
    return entrances

def bfs(x, y, keys, doors, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and board[nx][ny] != '*':
                visited[nx][ny] = 1
                if board[nx][ny] == '.' or board[nx][ny] == '$':
                    queue.append((nx, ny))
                    board[nx][ny] = '.'

                # 대문자
                elif board[nx][ny].isupper():
                    door = board[nx][ny]
                    key = door.lower()
                    doors[door] = True
                    if keys[key]:
                        queue.append((nx, ny))
                        board[nx][ny] = '.'
                        del doors[door]

                # 소문자
                elif board[nx][ny].islower():
                    key = board[nx][ny]
                    door = key.upper()    
                    keys[key] = True
                    queue.append((nx, ny))
                    board[nx][ny] = '.'
                    # 열쇠를 발견하고 탐색 과정에서 열쇠에 맞는 문이 존재한다면 입구를 찾는 것부터 다시 실행한다. 
                    if doors[door]:
                        return find_documents(board, keys, doors)


def find_documents(board, keys, doors):
    entrances = into_building(board, keys, doors)
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for enter in entrances:
        x, y = enter
        bfs(x, y, keys, doors, visited)

# 현재 빌딩에 남아있는 문서의 개수를 파악한다. 처음과 마지막 문서의 개수를 얻는데 사용하여 획득한 문서의 개수를 얻도록 한다. 
def get_document(board):
    document = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == '$':
                document += 1
    return document

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    total_document = get_document(board)

    words = list(input().rstrip())
    keys = defaultdict(bool)
    for word in words:
        keys[word] = True

    doors = defaultdict(bool)
    
    find_documents(board, keys, doors)

    residue_document = get_document(board)

    document = total_document - residue_document

    print(document)
