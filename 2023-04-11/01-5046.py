import sys
input = sys.stdin.readline

N, B, H, W = map(int, input().split())

min_cost = B + 1
for _ in range(H):
    p = int(input())
    nums = list(map(int, input().split()))
    for x in nums:
        if x >= N:
            cost = N * p 
            min_cost = min(min_cost, cost)
    
if min_cost <= B:
    print(min_cost)
else:
    print("stay home")



