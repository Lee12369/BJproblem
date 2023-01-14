N = int(input())
for i in range(N):
    OX = list(input().replace('X',' ').split())
    Sum_point = 0
    for i in range(len(OX)):   
        cts =  OX[i].count('O')
        point = int((cts*(cts+1))/2)
        Sum_point += point
    print(Sum_point)