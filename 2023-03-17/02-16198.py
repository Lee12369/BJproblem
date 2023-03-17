import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

score = 0
ans_lst = []
def back_tracking(N, score, nums):
    if len(nums) == 2:
        ans_lst.append(score)
        return 0

    for i in range(1, N - 1):
        save_nums = nums[:i] + nums[i + 1:]
        save_N = N - 1
        save_score = score + nums[i - 1] * nums[i + 1]

        back_tracking(save_N, save_score, save_nums)

back_tracking(N, score, nums)

ans = max(ans_lst)

print(ans)