from collections import deque
N = int(input())

queue = deque(range(1, N + 1))
bin_list = deque()
while queue:
    bin_list.append(queue.popleft())
    queue.rotate(-1)

for x in bin_list:
    print(x, end=' ')