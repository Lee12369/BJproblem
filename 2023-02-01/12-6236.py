N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]

left = 0
right = 10000
while True:
    mid = (left + right) // 2
    money = 0
    cnt = 0
    if left == mid:
        break

    for x in nums:
        if money >= x:
            money -= x
        else:
            money = 0
            while money < x:
                cnt += 1
                money += mid
            money -= x

    if cnt <= M:
        right = mid
    
    elif cnt > M:
        left = mid

print(right)