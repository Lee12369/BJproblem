# 런타임 오류 발생

from statistics import median
import sys
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
# 산술평균
sum_1 = 0
for x in numbers:
    sum_1 += x
answer_1 = round(sum_1/N)

# 중앙값
answer_2 = median(numbers)


# 최빈값
dic = {}

for key in numbers:
    dic[key] = 0

for key in numbers:    
    if key in dic:
        dic[key] += 1

freq_items = list(dic.items())
freq_val = list(dic.values())
max_freq = max(freq_val)
max_index = freq_val.index(max_freq)
cts = freq_val.count(max_freq) 

if cts > 1:
    rank = [0 for _ in range(cts)]
    for i in range(len(freq_items)):
        if freq_items[i][1] == max_freq:
            rank[i] = freq_items[i][0] 
    
    rank.remove(min(rank))
    answer_3 = min(rank)

else :
    answer_3 = freq_items[max_index][0]


# 범위
answer_4 = max(numbers) - min(numbers)

answers = [answer_1, answer_2, answer_3, answer_4]
for i in answers:
    print(i)