import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []
def back_tracking(start, lst):
    if len(lst) == M:
        for x in lst:
            print(x, end = ' ')
        print()
        return 0
    
    for i in range(start, N + 1):
        lst.append(i)
        back_tracking(i, lst)
        lst.pop()

back_tracking(1, lst)