N = int(input())

grades = list(map(int, input().split()))

answer = max(grades) - min(grades)

print(answer)