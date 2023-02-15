N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

coin = 0
for i in range(N - 1, -1, -1):
    coin += K // nums[i]
    K %= nums[i]
    if K == 0:
        break

print(coin)