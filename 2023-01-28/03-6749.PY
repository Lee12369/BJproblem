N, M = [int(input()) for _ in range(2)]

answer = max(N, M) + abs(N - M)

print(answer)