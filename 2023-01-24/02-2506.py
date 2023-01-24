N = int(input())
lst = list(map(int, input().split()))

answer = []

pre = 0
for i in range(N):
    if lst[i] == 1 and pre == 0:
        answer.append(1)
    
    elif lst[i] == 1 and pre == 1:
        answer.append(answer[i-1] + 1)
    
    else:
        answer.append(0)
    
    pre = lst[i]

print(sum(answer))
