import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = [input().rstrip('\n').split() for _ in range(N)]
    
    arr.sort(key= lambda x : int(x[1]), reverse=True)
   
    print(arr[0][0])
