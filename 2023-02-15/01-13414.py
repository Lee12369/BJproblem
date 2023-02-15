from collections import defaultdict
import sys
input = sys.stdin.readline

K, L = map(int, input().split())
nums = [input().rstrip('\n') for _ in range(L)]

dic = defaultdict(int)

M = 1
for N in nums:
    dic[N] = M
    M += 1

lst = list(dic.items())
lst.sort(key = lambda x: x[1])

if K > len(lst):
    K = len(lst)

answer = [lst[i][0] for i in range(K)]

for ans in answer:
    print(ans)