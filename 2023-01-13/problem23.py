import sys
iter_num = int(input(''))
for i in range(iter_num):
    A, B = map(int,sys.stdin.readline().split())
    print(A+B)