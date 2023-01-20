import sys
N = int(input())
for _ in range(N):
    lst = list(sys.stdin.readline().split())
    M = len(lst)
    
    for i in range(M):
        rev_list = list(reversed(lst[i]))

        for j in rev_list:
            print(j, end='')
        
        print(end=' ')
    
    print()