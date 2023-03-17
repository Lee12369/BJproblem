import math
N, M = map(int, input().split())

nums = list(map(int, input().split()))

cnt = 0
weight = 0
ans_lst = []

def back_tracking(start, weight, cnt):
    if cnt == M:
        # 1 이상의 값을 저장
        if weight > 1:
            ans_lst.append(weight)
        return 0
    
    for i in range(start, N):
        save_weight = weight + nums[i]
        save_cnt = cnt + 1

        back_tracking(i + 1, save_weight, save_cnt)

back_tracking(0, weight, cnt)

ans_lst = list(dict.fromkeys(ans_lst))

prime_nums = []
for x in ans_lst:
    check = 1
    # 2의 경우 소수이기 때문에 예외 처리.
    if x > 2:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                check = 0
                break
    if check == 1:
        prime_nums.append(x)

prime_nums.sort()

if prime_nums:
    for x in prime_nums:
        print(x, end=' ')

else:
    print(-1)