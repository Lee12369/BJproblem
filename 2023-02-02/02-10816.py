import sys    
input = sys.stdin.readline

def get_start(A, N, x):
    left = - 0 
    right =  N - 1
    while True:
        mid = (left + right) // 2
        mid_num = A[mid]
        if mid == left:
            if A[left] != x and A[right] != x:
                return 0
            
            elif A[left] == A[right]:
                return left
                
            elif A[left] != A[right]:
                return right
            
        if x <= mid_num:
            right = mid
        
        elif x > mid_num:
            left = mid

def get_end(A, N, x):
    left = - 0 
    right =  N - 1
    while True:
        mid = (left + right) // 2
        mid_num = A[mid]
        if mid == left:
            if A[left] != x and A[right] != x:
                return 0
            
            elif A[left] == A[right]:
                return right + 1

            elif A[left] != A[right]:
                return left + 1

        if x < mid_num:
            right = mid
        
        elif x >= mid_num:
            left = mid

N = int(input())
A = list(map(int, input().rstrip('\n').split()))
A.sort()

M = int(input())
nums = list(map(int, input().rstrip('\n').split()))

for x in nums:
    cnt = get_end(A, N, x) - get_start(A, N, x)
    print(cnt, end=' ')