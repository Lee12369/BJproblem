import sys
input = sys.stdin.readline

look_x = [-1, 0, 1, 0]
look_y = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    words = input()
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    x = 0
    y = 0
    look = 0
    for word in words:
        if word == 'F':
            x += look_x[look]
            y += look_y[look]
        
        elif word == 'B':
            x -= look_x[look]
            y -= look_y[look]
        
        elif word == 'L':
            look -= 1
            if look < 0:
                look += 4

        elif word == 'R':
            look += 1
            if look > 3:
                look -= 4
        
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    ans = (max_x - min_x) * (max_y - min_y)

    print(ans)