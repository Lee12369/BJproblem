N = int(input())

left = 1
right = 1
sum_num = 1
cnt = 0
while True:
    if sum_num < N:
        right += 1
        sum_num += right
    
    elif sum_num > N:
        sum_num -= left 
        left += 1
    
    elif sum_num == N:
        cnt += 1
        sum_num -= left
        left += 1

    if left == right:
        if N == 1:
            cnt = 1
        else:
            cnt += 1
        break

print(cnt)