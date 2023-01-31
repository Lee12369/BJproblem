T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    
    answer = N + M

    print("Case {}: {}".format(i, answer))