from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def bfs(dic, visited=[]):
    cnt = 0
    for x in all_nums:
        queue = deque()
        if x not in visited:
            queue.append(x)
            cnt += 1
        while queue:
            K = queue.popleft()
            if K not in visited:
                visited.append(K)
                for y in dic[K]:
                    queue.append(y)
    return cnt

N, M = map(int, input().split())

dic = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a] += [b]
    dic[b] += [a]

all_nums = [i for i in range(1, N + 1)]
answer = bfs(dic)

print(answer)
