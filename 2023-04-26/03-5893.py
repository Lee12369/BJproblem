N = input()

# 10진수로 변환 후 17을 곱한다.
M = int(N, 2) * 17

# 다시 2진수로 변환
ans = bin(M)[2:]

print(ans)
