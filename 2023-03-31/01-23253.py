import sys
input = sys.stdin.readline

N, M = map(int, input().split())
books = []
for _ in range(M):
    _ = input()
    dummy = list(map(int, input().strip().split()))
    books.append(dummy)


for lst in books:
    is_possible = "Yes"
    temp = sorted(lst, reverse=True)
    if lst != temp:
        is_possible = "No"
        break

print(is_possible)

