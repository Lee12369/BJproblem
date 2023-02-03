import sys
input = sys.stdin.readline

def get_style(styles, N, x):
    left = 0
    right = N -1 

    while True:
        mid = (left + right) // 2
        mid_power = int(styles[mid][1])

        if mid == left:
            if left == 0 and x <= int(styles[0][1]):
                return styles[0][0]
            else:
                return styles[right][0]
            

        if x <= mid_power:
            right = mid

        elif x > mid_power:
            left = mid


N, M = map(int, input().rstrip('\n').split())
styles = [input().rstrip('\n').split() for _ in range(N)]
powers = [int(input()) for _ in range(M)]

for x in powers:
    style = get_style(styles, N, x)
    print(style)