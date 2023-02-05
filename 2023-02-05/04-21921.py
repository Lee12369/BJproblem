import sys
input = sys.stdin.readline
N, X = map(int, input().rstrip('\n').split())
visit_nums = list(map(int, input().rstrip('\n').split()))

start = X - 1
pre = sum(visit_nums[:X])
max_num = pre
cnt = 1
for i in range(start + 1, N):
    curr = pre - visit_nums[i - X] + visit_nums[i]
    
    if curr > max_num:
        max_num = curr
        cnt = 1
    elif curr == max_num:
        cnt += 1
    
    pre = curr

if max(visit_nums) != 0:
    print(max_num)
    print(cnt)

else:
    print("SAD")