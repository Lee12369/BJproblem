from collections import defaultdict
dic_cnt = defaultdict(int)
dic_time = defaultdict(int)

N = int(input())
M = int(input())
nums = list(map(int, input().split()))

# N = 3
# M = 9
# nums = [2,1,4,3,5,6,2,7,2]
time = 1
for x in nums:
    dic_cnt[x] += 1
    if dic_cnt[x] == 1 and dic_time[x] == 0:
        dic_time[x] = time
    
    cnt_lst = list(dic_cnt.values())
    cnt_lst.sort(reverse = True)
  
    if len(cnt_lst) > N and cnt_lst[N - 1] == cnt_lst[N]:
        temp_lst = [key for key, val in dic_cnt.items() if val == cnt_lst[N]]
        
        min_time = dic_time[temp_lst[0]]
        del_target = temp_lst[0]
        for y in temp_lst:
            if dic_time[y] < min_time:
                min_time = dic_time[y]
                del_target = y

        del dic_cnt[del_target]
        del dic_time[del_target]

    time += 1 

answer = list(dic_cnt.keys())[0:N]
answer.sort()

for x in answer:
    print(x, end = ' ')