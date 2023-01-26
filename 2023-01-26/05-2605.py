N = int(input())
lst = list(map(int, input().split()))

order = [0]

for idx, x in enumerate(lst):
    order.insert(x, idx + 1)

order.reverse()

for x in order[1:]:
    print(x, end=' ')
