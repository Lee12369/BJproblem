import sys

N = int(input())

switch = list(map(int, sys.stdin.readline().split()))

M = int(input())
for _ in range(M):
    gender, number = map(int, sys.stdin.readline().split())

    if gender == 1:
        share_switch = N // number
        for i in range(share_switch):
            idx = number * (i + 1) - 1
            if switch[idx]:
                switch[idx] = 0
            else:
                switch[idx] = 1
        
    else:
        if N // 2 >= number:
            K = number - 1
        else:
            K = N - number

        cnt = 0
        for i in range(1, K + 1):    
            if switch[number - 1 - i] == switch[number - 1 + i]:
                cnt += 1
            else:
                break

        for idx in range(number - 1 - cnt, number + cnt):
            if switch[idx]:
                switch[idx] = 0
            else:
                switch[idx] = 1

cnt = 0
for x in switch:
    print(x, end=' ')
    cnt += 1
    if cnt % 20 == 0:
        print()