nums = [int(input()) for _ in range(5)]

A, B, C, D, E = nums
if A < 0:
    time = abs(A) * C + D + B * E
elif A > 0:
    time = (B - A) * E

print(time)