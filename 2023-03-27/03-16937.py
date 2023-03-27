import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = [list(map(int, input().split())) for _ in range(N)]

idx_1 = [(0,0),(0,1),(1,0),(1,1)]
idx_2 = [(1,1),(1,0),(0,1),(0,0)]

def Check(lst_1, lst_2, max_square):
    for i in range(4):    
        length_1 = lst_1[idx_1[i][0]] + lst_2[idx_1[i][1]]
        length_2 = max(lst_1[idx_2[i][0]], lst_2[idx_2[i][1]])

        if (length_1 <= W and length_2 <= H) or (length_1 <= H and length_2 <= W):
            square = (lst_1[0] * lst_1[1]) + (lst_2[0] * lst_2[1])

            max_square = max(max_square, square)

    return max_square

max_square = 0
for i in range(N):
    for j in range(i + 1, N):
        max_square = Check(stickers[i], stickers[j], max_square)

print(max_square)