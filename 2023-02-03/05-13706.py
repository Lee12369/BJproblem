N = int(input())

left = 0
right = 10 ** 400

while True:
    mid = (left + right) // 2
    mid_square = mid ** 2

    if mid_square > N:
        right = mid

    elif mid_square < N:
        left = mid

    elif mid_square == N:
        print(mid)
        break