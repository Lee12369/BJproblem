# 예제는 맞는데 제출하니까 틀렸다고 나옴.
# 포기, 다른 풀이 방법 있으면 알려줘.

from collections import deque

re = int(input())
Answer = []
for _ in range(re):
    N, M = map(int,input().split())
    numbers = deque(map(int,input().split()))
    if N != len(numbers):
        break

    curr_index = M
    cts = 0
    
    for _ in range(N):
        max_index = numbers.index(max(numbers))
        numbers.rotate(max_index)
        numbers.popleft()
        
        N -= 1
        cts += 1
        if curr_index == max_index:
            break
        
        curr_index -= max_index + 1
        if curr_index < 0 :
            curr_index += N
    
    print(cts)

