import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int ,input().split()))

snow = 1
curr = -1
cnt = 0
ans_lst = []
def back_tracking(snow, curr, cnt):
    if cnt == M or curr == N - 1:
        ans_lst.append(snow)
        return 0
    
    if curr < N - 1:
        next = curr + 1
        next_snow = snow + nums[next]
        next_cnt = cnt + 1
        
        back_tracking(next_snow, next, next_cnt)

    if curr < N - 2:
        next = curr + 2    
        next_snow = snow // 2 + nums[next]
        next_cnt = cnt + 1

        back_tracking(next_snow, next, next_cnt)


back_tracking(snow, curr, cnt)

print(max(ans_lst))