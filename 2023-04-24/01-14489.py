A, B = map(int, input().split())
chicken_cost = int(input())

N = A + B - chicken_cost * 2
if N >= 0:
    ans = N
else:
    ans = A + B

print(ans)