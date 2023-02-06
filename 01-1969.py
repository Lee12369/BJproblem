N, M = map(int, input().split())
words = [list(input()) for _ in range(N)]

words_column = list(map(list, zip(*words)))
answer = ''
for list in words_column:
    dic = {
        'A' : 0,
        'C' : 0,
        'G' : 0,
        'T' : 0
        }
    for x in list:
        dic[x] += 1
    
    max_val = 0
    for key, val in dic.items():
        if val > max_val:
            max_val = val
            get_word = key

    answer = answer + get_word

cnt = 0
for i in range(M):
    for j in range(N):
        if answer[i] != words_column[i][j]:
            cnt += 1

print(answer)
print(cnt)