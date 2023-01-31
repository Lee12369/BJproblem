A, B = map(int, input().split())
max_n = max(A, B)
min_n = min(A, B)

if max_n != min_n:
    cnt = max_n - min_n - 1
else:
    cnt = 0

nums = [i for i in range(min_n + 1, max_n)]

print(cnt)
for x in nums:
    print(x, end=' ')
