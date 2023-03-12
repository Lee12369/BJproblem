import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
score = 0
lst = []

def back_tracking(score, start, lst):
    global cnt
    if lst and score == S:
        cnt += 1

    for i in range(start, N):
        score += nums[i]
        lst.append(nums[i])

        back_tracking(score, i + 1, lst)
        
        score -= nums[i]
        lst.pop()

back_tracking(score, 0, lst)

print(cnt)