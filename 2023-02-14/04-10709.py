import sys
input = sys.stdin.readline

H, W = map(int, input().split())
arr = [list(input().rstrip('\n')) for _ in range(H)]

for i in range(H):
    j = 0
    while j < W:
        if arr[i][j] == '.':
            arr[i][j] = -1
            j += 1
        
        else:
            arr[i][j] = 0
            j += 1
            while j < W and arr[i][j] == '.':
                arr[i][j] = arr[i][j - 1] + 1     
                j += 1

for lst in arr:
    for x in lst:
        print(x, end=' ')
    print()
        

