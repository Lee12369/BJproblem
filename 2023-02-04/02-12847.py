n, m = map(int, input().split())

wages = list(map(int, input().split()))

# i = 0
pre_wage = sum(wages[:m])
max_wage = pre_wage
for i in range(1, n - m + 1):
    sum_wage = pre_wage - wages[i - 1] + wages[i + m - 1]
    max_wage = max(max_wage, sum_wage)
    pre_wage = sum_wage

print(max_wage)