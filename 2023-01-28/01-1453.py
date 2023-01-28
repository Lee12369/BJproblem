N = int(input())
number = set(map(int, input().split()))

answer = N - len(number)

print(answer)
