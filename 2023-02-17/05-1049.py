import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cost_bundle = 1000
cost_single = 1000
for _ in range(M):
    bundle, single = map(int, input().split())
    cost_bundle = min(cost_bundle, bundle)
    cost_single = min(cost_single, single)

cnt_bundle = N // 6
cnt_single = N % 6

cost_1 = cost_bundle * cnt_bundle + cost_single * cnt_single

if cnt_single == 0:
    cost_2 = cost_bundle * cnt_bundle
else:
    cost_2 = cost_bundle * (cnt_bundle + 1)

cost_3 = cost_single * N

ans = min(cost_1, cost_2, cost_3)

print(ans)