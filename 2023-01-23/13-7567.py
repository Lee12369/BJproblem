from collections import deque
queue = deque(input())

curr = ''
cts = 0
while queue:
    next = queue.popleft()
    if curr == next:
        cts += 5
    else:
        cts += 10
    
    curr = next

print(cts)