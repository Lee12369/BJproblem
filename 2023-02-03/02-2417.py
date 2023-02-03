n = int(input())

left = 0
right = 2 ** 63

while True:
    mid = (left + right) // 2
    mid_num = mid ** 2
    
    if mid == left:
        if mid_num == n:
            print(mid)
        else:
            print(right)
        break

    if mid_num > n:
        right = mid

    elif mid_num < n:
        left = mid
    
    elif mid_num == n:
        print(mid)
        break