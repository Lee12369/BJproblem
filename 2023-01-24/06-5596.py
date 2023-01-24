N = map(int, input().split())
M = map(int, input().split())

sum_N = sum(N)
sum_M = sum(M)

answer = max(sum_N, sum_M)

print(answer)