import sys
dic = {
    0 : [10],
    1 : [1],
    2 : [2, 4, 8, 6],
    3 : [3, 9, 7, 1],
    4 : [4, 6],
    5 : [5],
    6 : [6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9 : [9, 1]
}

N = int(input())

for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    one_digit = lst[0] % 10
    value = dic.get(one_digit)
    index = lst[1] % len(value)
    
    if index == 0:
        print(value[-1])
    else :
        print(value[index-1])
        