import sys
S =set()
M = int(input())
for i in range(M):
    
    lst = sys.stdin.readline().split()
    func = lst[0]
    
    if func == 'add':
        S.add(int(lst[1]))
    
    if func =='remove':
        S.discard(int(lst[1]))
        
    if func == 'check':
        len_S = len(S)
        S.add(int(lst[1]))
        len_append_S = len(S)
        
        if len_S == len_append_S:
            print(1)
        else:
            print(0)
            S.remove(int(lst[1]))

    if func == 'toggle':
        len_S = len(S)
        S.add(int(lst[1]))
        len_append_S = len(S)
        if len_S == len_append_S:
            S.remove(int(lst[1]))

    if func == 'all':
        S = {i for i in range(1,21)}

    if func == 'empty':
        S.clear()