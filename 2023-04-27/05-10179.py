import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    price = float(input()) * 0.8
    print("${:.2f}".format(price))
