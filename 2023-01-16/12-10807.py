N = int(input())
lst = list(map(int, input().split()))
v = int(input())
cnt = 0
for x in lst:
    if v == x:
        cnt += 1
print(cnt)