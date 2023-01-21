# 314 -->> 11001100, 8진수를 2진수로
N = input()
M =  int(N, 8)

answer = bin(M)[2:]

print(answer)