import sys
import itertools
input = sys.stdin.readline
N = int(input())
temp = [i for i in range(1, 10)]
nums = list(map(list, itertools.permutations(temp,3)))
break_cnt = 0

def get_cnt(nums):
    global N
    number_3, strike, ball = map(int, input().rstrip('\n').split())        
    number_3 = list(map(int, str(number_3)))

    able_nums = nums
    pass_nums = []
    for lst in able_nums:
        cnt_ball = 0
        cnt_strike = 0

        for i in range(3):
            if number_3[i] == lst[i]:
                cnt_strike += 1  
            elif number_3[i] in lst:
                cnt_ball += 1

           
        if ball == cnt_ball and strike == cnt_strike:
            pass_nums.append(lst)
 
    N -= 1
    if N == 0:
        return pass_nums

    return get_cnt(pass_nums)

answer = len(get_cnt(nums))

print(answer)