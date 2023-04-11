import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

lst_word = []
# 가로 
for i in range(N):
    lst_word.extend(board[i].split('#'))

# 세로
for j in range(M):
    word = ''
    for i in range(N):
        word += board[i][j]
    lst_word.extend(word.split('#'))

lst_word.sort()
for word in lst_word:
    if len(word) >= 2:
        print(word)
        break
    