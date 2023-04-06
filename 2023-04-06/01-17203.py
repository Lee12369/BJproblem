N, Q = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(Q):
    start, end = map(int, input().split())
    
    new_nums = nums[start - 1: end]

    ans = 0
    M = end - start
    for i in range(M):
      ans += abs(new_nums[i + 1] - new_nums[i])

    print(ans)