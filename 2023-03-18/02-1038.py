import sys
input = sys.stdin.readline

N = int(input())
nums = [str(i) for i in range(10)]

def back_tracking(string_num, length):
    if length < M:
        ans_lst.append(string_num)
        return

    for i in range(10):
        if nums[i] < int(string_num[-1]):
            save_string_num = string_num + str(nums[i])
            save_length = length + 1
            
            back_tracking(save_string_num, save_length)

ans_lst = [i for i in range(10)]
for M in range(2, 7):
    for i in range(10):
        length = 1
        back_tracking(str(i), length)

print(ans_lst)