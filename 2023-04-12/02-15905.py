N = int(input())
lst = []
for _ in range(N):
    problem, penalty = map(int, input().split())
    lst.append((problem, penalty))

lst.sort(key=lambda x : (-x[0], x[1]))
same_problem = lst[4][0]
coupon = 0
for i in range(5, N):
    if lst[i][0] == same_problem:
        coupon += 1
    else:
        break

print(coupon)