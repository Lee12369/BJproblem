from collections import deque

N, M = map(int, input().split())
lst = [i for i in range(2, N+1)]
queue = deque()

while lst:
    P = lst[0]
    
    for x in lst:
        if x % P == 0:
            lst.remove(x)
            queue.append(x)


queue.rotate(-M + 1)
answer = queue.popleft()

print(answer)