import sys
import math
def func1(lst: list):
    answer = round(sum(lst)/len(lst))
    return answer

def func2(lst:list):
    answer = sorted(lst)[math.floor(len(lst)/2)]
    return answer

def func3(lst):
    dic = {}
    for key in lst:
        dic[key] = 0

    for key in lst:    
        dic[key] += 1
    
    list_values = dic.values()
    max_value = max(list_values)
    list_items = list(dic.items())
    
    rank = []
    for i in range(len(list_items)):
        if list_items[i][1] == max_value:
            rank.append(list_items[i][0])
    
    rank = sorted(rank)
    if len(rank) == 1:
        answer = rank[0]

    else:
        answer = rank[1] 

    return answer

def func4(lst:list):
    answer = max(lst) - min(lst)
    return answer


N = int(input())
list_numbers = [0 for _ in range(N)]
for i in range(N):
    list_numbers[i] = int(sys.stdin.readline())

answer_1 = func1(list_numbers)
answer_2 = func2(list_numbers)
answer_3 = func3(list_numbers)
answer_4 = func4(list_numbers)

print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)


