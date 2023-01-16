from collections import deque
N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
answer = []
# for i in range(N):
while queue:
    queue.rotate(-(K - 1))
    answer.append(queue.popleft())

print('<', end ='')
for i in answer:
    if i == answer[-1]:
        print(i, end='')
        break
    print(i,end=', ')
print('>')