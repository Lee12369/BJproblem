import sys
input = sys.stdin.readline

def get_cnt(B, M, x):
        left = 0
        right = M - 1
        while True:
            mid = (left + right) // 2 
            mid_num = B[mid]
            if mid == left:
               if x > B[right]:
                    return right + 1 

               elif B[left] < x <= B[right]:
                    return right

               else:
                    return 0
               
            if x > mid_num:
                left = mid

            elif x <= mid_num:
                right = mid


T = int(input())

for _ in range(T):
    N, M = map(int, input().rstrip('\n').split())
    A = list(map(int, input().rstrip('\n').split()))
    B = list(map(int, input().rstrip('\n').split()))
    
    B.sort()
    cnt = 0
    for x in A:
        cnt += get_cnt(B,M,x)
    
    print(cnt)