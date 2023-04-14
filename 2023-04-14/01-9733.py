from collections import defaultdict
import math

cnt = 0
dic = defaultdict(int)
while True:
    try:
        actions = list(input().split())
        for x in actions:
            dic[x] += 1
            cnt += 1
    except:
        break

dic['Total'] = cnt

keys = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex', 'Total']
for key in keys:
    ratio = dic[key] / cnt
    print('{} {} {:.2f}'.format(key, dic[key], ratio))


