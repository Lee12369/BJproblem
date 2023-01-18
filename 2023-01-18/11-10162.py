lst = [300, 60, 10]
N = int(input())
Answer_dic = {}

for x in lst:
    Answer_dic[x] = N // x
    N -= x * Answer_dic[x]

Answer_list = Answer_dic.values()

if N:
    print(-1)
else:
    for y in Answer_list:
        print(y, end=' ')
