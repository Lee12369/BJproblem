import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    
    arr =[input().split() for _ in range(N)]
    arr.sort(key=lambda x: -int(x[0]))
    
    print(arr[0][1])