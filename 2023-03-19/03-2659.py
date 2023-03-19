clock_number = list(input().split())

numbers = []
for i in range(4):
    clock = ''
    for j in range(4):
        clock += clock_number[i + j - 3]
    numbers.append(int(clock))

min_num = min(numbers) 

nums = [str(i) for i in range(1, 10)]

number = ''
start = 0
cnt = 0
ans_lst = []
def back_tracking(start, number, cnt):
    if cnt == 4:
        ans_lst.append(int(number))
        return
    
    for i in range(start, 9):
        save_number = number + nums[i]
        save_cnt = cnt + 1
        
        back_tracking(i, save_number, save_cnt)

back_tracking(start, number, cnt)

ans = ans_lst.index(min_num) + 1

print(ans_lst)
print(ans)