from collections import deque
N = int(input())
nums = [i for i in range(1, N + 1)]
queue = deque(nums)

M = len(nums)
for i in range(1, N):
    delete_num = i ** 3

    queue.rotate(-(delete_num % M - 1))
    queue.popleft()

    M -= 1

ans = queue.pop()

print(ans)