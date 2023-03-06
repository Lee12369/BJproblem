from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = list(input())
    N = int(input())
    if N == 0:
        _ = input()
        lst = []
    else:
        lst = list(map(int, input().rstrip("\n").strip("[").strip("]").split(',')))
    
    if P.count('D') > N:
        print("error")
        continue

    start_idx = 0
    end_idx = N
    i = 0
    R_num = 0
    while i < len(P):
        if P[i] == 'R':
            R_num += 1

        if P[i] == 'D':
            if R_num % 2 == 0:
                start_idx += 1
            else:
                end_idx -= 1
        i += 1
    
    if R_num % 2 == 1:
        ans_lst = list(reversed(lst[start_idx : end_idx]))
    else:
        ans_lst = lst[start_idx : end_idx]

    len_ans = len(ans_lst)
    print("[", end='')
    for i in range(len_ans):
        if i < len_ans - 1:
            print(ans_lst[i], end=',')
        else:
            print(ans_lst[i], end='')
    print("]")
