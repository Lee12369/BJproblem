import sys

T = int(input())

for _ in range(T):
    _ = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    
    answer = sum(lst)
    
    print(answer)
