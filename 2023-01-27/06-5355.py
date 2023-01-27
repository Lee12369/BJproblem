import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    lst = list(input().rstrip('\n').split())
    num = float(lst[0])
    for x in lst[1:]:
        if x == '@':
            num *= 3
    
        elif x == '%':
            num += 5
        
        elif x == '#':
            num -= 7

    print("{:.2f}".format(num))