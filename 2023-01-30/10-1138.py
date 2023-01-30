N = int(input())

line = [10 for _ in range(N)]

left_higher_nums = list(map(int, input().split()))

num = 1
for x in left_higher_nums:
    for i in range(N):
        if line[i] == 10 and line[:i].count(10) == x:
            line[i] = num
            num += 1
            break

for x in line:
    print(x, end=' ')