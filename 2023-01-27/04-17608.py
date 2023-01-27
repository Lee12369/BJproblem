import sys
input = sys.stdin.readline
N = int(input())

lst = [0]
for _ in range(N):
    curr = int(input())
    
    while len(lst) > 0 and curr >= lst[-1]: 
        lst.pop()
    
    lst.append(curr)

answer = len(lst)

print(answer)