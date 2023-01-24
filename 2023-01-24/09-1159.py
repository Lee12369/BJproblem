import sys
N = int(input())
lst = [list(sys.stdin.readline()) for _ in range(N)]

dic = {}

for x in lst:
    if x[0] not in dic.keys():
        dic[x[0]] = 1

    else:
        dic[x[0]] += 1

answer = []

for key, val in dic.items():
    if val >= 5:
        answer.append(key)

answer.sort()


if answer:
    for x in answer:
        print(x, end='')
        
else:
    print("PREDAJA")