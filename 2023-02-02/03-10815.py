import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().rstrip('\n').split()))
A.sort()

M = int(input())
nums = list(map(int, input().rstrip('\n').split()))

def get_in_check(A, N, x):
    left = - 0 
    right =  N - 1 
    while True:
        mid = (left + right) // 2
        mid_num = A[mid]
        if mid == left:
            if x == A[left] or x == A[right]: 
                return 1
            else:
                return 0

        if x < mid_num:
            right = mid
        
        elif x > mid_num:
            left = mid

        elif x == mid_num:
            return 1

for x in nums:
    print(get_in_check(A,N,x), end=' ')
