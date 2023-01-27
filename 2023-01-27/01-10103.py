import sys
input = sys.stdin.readline
N = int(input())
score_A = score_B = 100

for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        score_B -= A
    
    if B > A:
        score_A -= B

print(score_A)
print(score_B)

