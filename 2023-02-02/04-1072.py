X, Y = map(int, input().split())

Z = (Y * 100) // X
left = 0
right = 10 ** 9 + 1
while True:
    mid = (left + right) // 2
    mid_num = ((Y + mid) * 100) // (X + mid)

    if mid == left:
        right_num = ((Y + right) * 100) // (X + right)
        if Z != right_num:
            answer = right
        else:
            answer = -1
        break


    if mid_num > Z:
        right = mid

    elif mid_num <= Z:
        left = mid

print(answer)
