import sys
input = sys.stdin.readline
N, M = map(int, input().split())

A = list(map(int, input().rstrip('\n').split()))
B = list(map(int, input().rstrip('\n').split()))

point_A = 0
point_B = 0

answer = []

while point_A < len(A) and point_B < len(B):
    num_A = A[point_A]
    num_B = B[point_B]
    
    if num_A <= num_B:
        point_A += 1
        answer.append(num_A)
        
    elif num_A > num_B:
        point_B += 1
        answer.append(num_B)

answer = answer + A[point_A:] + B[point_B:]

for ans in answer:
    print(ans, end=' ')       
