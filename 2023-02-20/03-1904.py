N = int(input())

if N > 2:
    pre_1 = 2
    pre_2 = 1

    for _ in range(N - 2):
        curr = (pre_1 + pre_2) % 15746
        pre_1, pre_2 = curr, pre_1

else:
    curr = N

ans = curr % 15746

print(ans)