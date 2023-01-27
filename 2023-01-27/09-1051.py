import sys
input = sys.stdin.readline

def get_max_square():
    global max_square, square
    for k in range(j+1, M):
        if arr[i][j] == arr[i][k]:
            width = k - j + 1
            if width <= (N - i) and arr[i][j] == arr[i + width - 1][j] == arr[i + width - 1][k]:
                square = width ** 2
                max_square = max(square, max_square)
    return max_square

N, M = map(int, input().split())
arr = [list(map(int, list(input().rstrip('\n')))) for _ in range(N)]

max_square_lst = []
for i in range(N):
    for j in range(M):
        square = max_square = 1                

        max_square_lst.append(get_max_square())

answer = max(max_square_lst)

print(answer)

