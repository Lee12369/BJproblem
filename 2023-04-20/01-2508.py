def check_candy():
    candy = 0
    for i in range(R):
        for j in range(C - 2):
            if arr[i][j] == '>' and arr[i][j + 1] == 'o' and arr[i][j + 2] == '<':
                candy += 1
    
    for i in range(R - 2):
        for j in range(C):
            if arr[i][j] == 'v' and arr[i + 1][j] == 'o' and arr[i + 2][j] == '^':
                candy += 1
    
    return candy

T = int(input())

for _ in range(T):
    _ = input()
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]
    
    candy = check_candy()

    print(candy)