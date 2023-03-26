import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [float(input()) for _ in range(N)]
nums.sort()

# 절사 평균.
trimmed_nums = nums[K : N - K]
trimmed_avg = sum(trimmed_nums) / len(trimmed_nums) 
if trimmed_avg * 1000 % 10  >= 5:
    trimmed_avg += 0.0001

trimmed_avg = round(trimmed_avg, 2)
# 보정 편균
calibrated_avg = (trimmed_nums[0] * K + sum(trimmed_nums) + trimmed_nums[-1] * K ) / N 
if calibrated_avg * 1000 % 10  >= 5:
    calibrated_avg += 0.0001

calibrated_avg = round(calibrated_avg, 2)

print("{:.2f}".format(trimmed_avg))
print("{:.2f}".format(calibrated_avg))