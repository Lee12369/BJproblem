from collections import deque

re = int(input())
Answer = []
for _ in range(re):
    N, M = map(int,input().split())
    queue = deque(map(int,input().split()))
    curr_index = M
    cts = 0
    
    for _ in range(N):
        max_number = max(queue)
        max_index = queue.index(max_number)
        
        if curr_index == max_index:
            cts += 1
            break
        
        queue.rotate(-max_index)
        curr_index -= max_index
        
        if curr_index < 0 :
            curr_index += N
        
        queue.popleft()
        N -= 1
        cts += 1
        curr_index -= 1

    print(cts)