import sys
input = sys.stdin.readline

def recurr(x, y, n):
    global cnt_m1, cnt_0, cnt_1
    check = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                check = -2
                break
    
    if check == -1:
        cnt_m1 += 1
    elif check == 0:
        cnt_0 += 1
    elif check == 1:
        cnt_1 += 1
    elif check == -2:
        n //= 3
        for i in range(3):
            for j in range(3):
                recurr(x + n * i, y + n * j, n)

N = int(input())
arr = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

cnt_m1 = 0
cnt_0 = 0
cnt_1 = 0

recurr(0, 0, N)

print(cnt_m1) 
print(cnt_0)
print(cnt_1)       