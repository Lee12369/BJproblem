dic = {}
for i in range(10):
    dic[i] = str(i)

for i in range(65,91):
    dic[i -55] = chr(i)

N, B = map(int,input().split())

answer = []

while N:
    N, res = divmod(N, B)
    answer.append(dic[res])

answer.reverse()

for x in answer:
    print(x, end='')
