import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

lst_word = []

# 가로
for i in range(N):
    words = board[i].split('#')    
    lst_word.extend(words)

#세로
for j in range(M):
    word = ''
    for i in range(N):
        word += board[i][j]
    
    words = word.split('#')
    lst_word.extend(words)


lst_word.sort()
for word in lst_word:
    if len(word) > 1:
        print(word)
        break