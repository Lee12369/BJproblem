word = input()

dic = {chr(x):0 for x in range(65,91)}

for x in word:
    if x in dic:
        dic[x] += 1

cnt = 0
lst = []
median = []
for key, val in dic.items():
    if val % 2 == 1:
        cnt += 1
        median = [key]

    val //= 2
 
    for _ in range(val):
        lst.append(key)

rev_lst = list(reversed(lst))
answer = lst + median + rev_lst

if cnt <= 1:
    for x in answer:
        print(x, end='')

else:
    print("I'm Sorry Hansoo")