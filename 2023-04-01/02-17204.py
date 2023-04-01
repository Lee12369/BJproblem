from collections import deque
N, K = map(int, input().split())

dic = {}
for i in range(N):
    point_out = int(input())
    dic[i] = point_out

visited = [0 for _ in range(N)]
call_num = 1

queue = deque()
queue.append(0)
while queue:
    call_person = queue.pop()
    if visited[call_person] == 0:
        visited[call_person] = call_num
        queue.append(dic[call_person])
        call_num += 1

if visited[K] > 0:
    print(visited[K] - 1) # M을 외친 사람이 벌주가 아니라 M 을 외친 사람이 지목한 상대가 벌주.

else:
    print(-1)