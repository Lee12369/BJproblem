import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X = int("".join(input().split()))
    Y = int("".join(input().split()))

    nums = list(input().split())
    cnt = 0
    for i in range(N):
        number = ''
        for j in range(M):
            number += nums[i + j - M]
        number = int(number)
        if X <= number <= Y:
            cnt += 1
    
    print(cnt)