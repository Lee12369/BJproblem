import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if N > 0:
    books_lst = list(map(int, input().split()))
    box = [M]

    for i in range(N):
        book = books_lst[i]
        if box[-1] >= book:
            box[-1] -= book
        else:
            box.append(M - book)

else:
    box = []

print(len(box))
