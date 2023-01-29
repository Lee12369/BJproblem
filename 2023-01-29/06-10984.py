import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    sum_C = 0
    sum_CxG = 0
    for _ in range(N):
        C, G = input().rstrip('\n').split()
        C = int(C)
        G = float(G)
        
        sum_C += C
        sum_CxG += C * G

    GPA = round(sum_CxG / sum_C, 1)
        
    print(sum_C, GPA)