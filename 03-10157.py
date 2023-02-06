C, R = map(int, input().split())
K = int(input())
arr = [[0 for _ in range(C)] for _ in range(R)]

i = R
j = 0
num = 0
width = R
height = C
while True:
    # 위로 이동
    if width <= 0:
        break
    for _ in range(width):
        i -= 1
        num += 1
        arr[i][j] = num
    
    # 오른쪽으로 이동
    if height <= 1:
        break
    for _ in range(height - 1):
        j += 1
        num += 1
        arr[i][j] = num 
    
    # 아래로 이동
    if width <= 1:
        break
    for _ in range(width - 1):
        i += 1
        num += 1
        arr[i][j] = num 
    
    # 왼쪽으로 이동    
    if height <= 2:
        break
    for _ in range(height - 2):
        j -= 1
        num += 1
        arr[i][j] = num 

    width -= 2
    height -= 2

    
answer = [(i,j) for i in range(R) for j in range(C) if arr[i][j] == K]

if answer:
    print(1 + answer[0][1], R - answer[0][0])
else:
    print('0')