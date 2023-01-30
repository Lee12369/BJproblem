nums = list(map(int, input().split()))

total = sum(nums)
min_score = min(nums)

if total >= 100:
    print("OK")

elif min_score == nums[0]:
    print("Soongsil")

elif min_score == nums[1]:
    print("Korea")

elif min_score == nums[2]:
    print("Hanyang")