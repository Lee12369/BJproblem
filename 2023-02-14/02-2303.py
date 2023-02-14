N = int(input())
lst_ans = []
who = 1
ans = 0
for _ in range(N):
    nums = list(map(int, input().split()))
    max_num = 0
    for i in range(3):
        first = nums[i]
        for j in range(i + 1, 4):
            second = nums[j]
            for k in range(j + 1, 5):
                third = nums[k]
                sum_nums = (first + second + third) % 10
                max_num = max(max_num, sum_nums)
    
    if max_num >= ans:
        ans = max_num
        ans_who = who

    who += 1

print(ans_who)
