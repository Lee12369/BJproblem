group_cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    check = 1
    arr = [list(input().split()) for _ in range(N)]

    print("Group {}".format(group_cnt))
    
    for i in range(N):
        for j in range(1, N):
            if arr[i][j] == 'N':
                check = 0
                print("{} was nasty about {}".format(arr[i - j][0] ,arr[i][0]))
    
    if check == 1:
        print("Nobody was nasty")

    group_cnt += 1
    print()
