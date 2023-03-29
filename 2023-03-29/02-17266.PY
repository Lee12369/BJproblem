N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

def two_pointer(num):
    start = 0
    for x in lamps:
        if x - num <= start:
            start = x + num + 1
        else:
            return start
        
    return start

left = 1
right = N

# 최소 높이인 1로 충분할 경우.
if two_pointer(left) > N:
    print(1)

else:
    while True:
        mid = (left + right) // 2
        print(left, right, mid)
        if left == mid:
            print(right)
            break

        start = two_pointer(mid)

        if start > N:
            right = mid
        else:
            left = mid
