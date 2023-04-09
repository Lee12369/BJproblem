word = list(input().split('K'))
N = len(word)

# 최대값
max_num = ''
for i in range(N - 1):
    cnt_M = word[i].count('M')
    max_num += '5'
    for _ in range(cnt_M):
        max_num += '0'

if word[-1]:
    cnt_M = word[-1].count('M')
    for _ in range(cnt_M):
        max_num += '1'

# 최소값
min_num = ''
for i in range(N - 1):
    cnt_M = word[i].count('M')
    if cnt_M > 0:
        min_num += '1'
        for _ in range(cnt_M - 1):
            min_num += '0' 
        min_num += '5'
    else:
        min_num += '5'

if word[-1]:
    cnt_M = word[-1].count('M')
    min_num += '1'
    for _ in range(cnt_M - 1):
        min_num += '0' 

print(max_num)
print(min_num)
