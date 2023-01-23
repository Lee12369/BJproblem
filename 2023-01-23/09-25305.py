N, k = map(int, input().split())
grades = list(map(int, input().split()))

grades.sort(reverse=True)

answer = grades[k - 1]

print(answer)
