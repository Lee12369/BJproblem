import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
def back_tracking(lst):
    if len(lst) == M:
        for x in lst:
            print(x, end=' ')
        print()
        return 0

    for i in range(1, N + 1):
        lst.append(i)
        back_tracking(lst)
        lst.pop()

back_tracking(lst)