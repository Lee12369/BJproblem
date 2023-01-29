alphabet = [chr(i) for i in range(97,123)]

dic_1st = {x:0 for x in alphabet}
dic_2nd = {x:0 for x in alphabet}

word_1st = list(input())

for x in word_1st:
    dic_1st[x] += 1
sum_1st = sum(list(dic_1st.values()))

word_2nd = list(input())
for x in word_2nd:
    dic_2nd[x] += 1
sum_2nd = sum(list(dic_2nd.values()))

min_val = [min(dic_1st[x], dic_2nd[x]) for x in alphabet]
sum_min_val = sum(min_val)

answer = (sum_1st - sum_min_val) + (sum_2nd - sum_min_val)

print(answer)