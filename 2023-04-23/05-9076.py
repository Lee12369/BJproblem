T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    
    # 오름차순으로 정렬 후, 처음과 끝을 제외한다.
    nums.sort()
    nums = nums[1:-1]
    
    N = max(nums) - min(nums)
    if N < 4:
        ans = sum(nums)
    
    else:
        ans = 'KIN'

    print(ans)