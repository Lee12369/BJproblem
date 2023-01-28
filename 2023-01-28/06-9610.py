import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

dic = {
    'Q1': 0,
    'Q2': 0,
    'Q3': 0,
    'Q4': 0,
    'AXIS': 0
}


for lst in arr:
    if lst[0] == 0 or lst[1] == 0:
        dic['AXIS'] += 1

    elif lst[0] > 0 and lst[1] > 0:
        dic['Q1'] += 1

    elif lst[0] < 0 and lst[1] > 0:
        dic['Q2'] += 1

    elif lst[0] < 0 and lst[1] < 0:
        dic['Q3'] += 1

    else:
        dic['Q4'] += 1

for key, val in dic.items():
    print("{}: {}".format(key, val))