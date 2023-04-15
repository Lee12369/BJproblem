from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    robots = [input() for _ in range(N)]
    
    M = len(robots[0])
    win_robot = [i for i in range(N)]
    for i in range(M):
        # 각 단어를 가진 인덱스 값을 저장
        R = []
        S = []
        P = []
        for x in win_robot:
            word = robots[x][i] 
            if word == 'R':
                R.append(x)

            elif word == 'S':
                S.append(x)

            elif word == 'P':
                P.append(x)
        
        if R and S and not P:
            win_robot = R
        
        elif S and P and not R:
            win_robot = S

        elif P and R and not S:
            win_robot = P
        
        if len(win_robot) == 1:
            break

    if len(win_robot) == 1:
        print(win_robot[0] + 1)

    else:
        print(0)