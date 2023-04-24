dic = {chr(i + 97) : 0 for i in range(26)}
while True:
    try:
        sentence = list(input().split())
        for word in sentence:
            for x in word:
                dic[x] += 1
    except:
        break

max_cnt = max(dic.values())
for key, val in dic.items():
    if val == max_cnt:
        print(key, end='')