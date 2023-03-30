N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

def two_pointer(num):
    start = 0
    for x in lamps:
        if x - num <= start:
            start = x + num
        else:
            return start
        
    return start

left = 0
right = N

while True:
    mid = (left + right) // 2
    if left == mid:
        print(right)
        break

    start = two_pointer(mid)

    if start >= N:
        right = mid
    else:
        left = mid
