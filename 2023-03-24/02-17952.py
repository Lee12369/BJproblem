import sys
input = sys.stdin.readline

N = int(input())

assign_lst = []
score = 0
for _ in range(N):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        lst[2] -= 1
        assign_lst.append(lst[1:])
    
    elif lst[0] == 0:
        if len(assign_lst) > 0:
            assign_lst[-1][1] -= 1
    
    if len(assign_lst) > 0 and assign_lst[-1][1] == 0:
        score += assign_lst[-1][0]
        assign_lst.pop()

print(score) 
