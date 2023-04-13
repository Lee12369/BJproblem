from collections import deque

N = int(input())
queue = deque()
for num in range(N, 0, -1):
    queue.appendleft(num)
    queue.rotate(num)

for x in queue:
    print(x, end=' ')


