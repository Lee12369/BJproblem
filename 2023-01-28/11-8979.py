import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip('\n').split())
dic = {}

for _ in range(N):
    country, gold, silver, bronze = input().split()
    dic[country] = [int(gold), int(silver), int(bronze)]

item = list(dic.items())
item_sort = sorted(item, key = lambda x: x[1], reverse = True)

K = str(K)
target = tuple([K, dic[K]])
idx = item_sort.index(target)

while idx != 0:
    if item_sort[idx][1] == item_sort[idx-1][1]:
        idx -= 1        
    else:
        break

answer = idx + 1

print(answer)