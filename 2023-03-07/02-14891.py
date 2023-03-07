import sys
from collections import deque
input = sys.stdin.readline

gears = [0]
for _ in range(4):
    gear = deque(list(input().strip()))
    gears.append(gear)

K = int(input())
for _ in range(K):
    gear_num, rotation = map(int, input().split())
    
    rot_cnt = [0 for _ in range(5)]
    rot_cnt[gear_num] += -rotation
    
    # 2, 6 번이 맞닿아 있다.
    right = gear_num
    while right < 4:
        if gears[right][2] != gears[right + 1][6]:
            rot_cnt[right + 1] += -rot_cnt[right]
            right += 1
        else:
            break

    left = gear_num
    while 1 < left:
        if gears[left][6] != gears[left - 1][2]:
            rot_cnt[left - 1] += -rot_cnt[left]
            left -= 1
        else:
            break

    for i in range(1, 5):
        gears[i].rotate(-rot_cnt[i])

ans = 0
for i in range(1, 5):
    ans += (2 ** (i - 1)) * int(gears[i][0])

print(ans)
            