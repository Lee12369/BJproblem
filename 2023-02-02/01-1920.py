import sys
input = sys.stdin.readline

def in_check(A, N, x):
    left = - 0 
    right =  N
    while True:
        mid = (left + right) // 2
        mid_num = A[mid]
        if mid == left:
            if x == A[left]: 
                return 1
            else:
                return 0
            
        if x < mid_num:
            right = mid
        
        elif x > mid_num:
            left = mid

        elif x == mid_num:
            return 1


N = int(input())
A = list(map(int, input().rstrip('\n').split()))
A.sort()

M = int(input())
nums = list(map(int, input().rstrip('\n').split()))


for x in nums:
    answer = in_check(A, N, x)
    print(answer)
