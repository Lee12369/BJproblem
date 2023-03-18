from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

dic = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

def back_tracking(start, lst, visited):
    if len(lst) == 5:
        ans_lst.append(True)
        return 1

    for x in dic[start]:
        if visited[x] == 0:
            visited[x] = 1
            save_lst = lst + [x]
            save_start = int(x)

            back_tracking(save_start, save_lst, visited)

            visited[x] = 0
            
for i in range(N):
    lst = [i]
    visited = [0 for _ in range(N)]
    visited[i] = 1
    ans_lst = []
    back_tracking(i, lst, visited)
    
    if ans_lst:
        print(1)
        break

if ans_lst == []:
    print(0)