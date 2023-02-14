N = int(input())
M = N + 1
nums = set()
for i in range(M):
    for j in range(i, M):
        for k in range(j, M):
            l = M - i - j - k - 1
            if l < 0:
                l = 0
            sum = i * 1 + (j - i) * 5 + (k - j) * 10 + (N - k) * 50
            nums.add(sum)

answer = len(nums)

print(answer)