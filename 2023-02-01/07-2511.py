A = list(map(int, input().split()))
B = list(map(int, input().split()))

win_lose_board = []
A_score = 0
B_score = 0
for i in range(10):
    if A[i] > B[i]:
        A_score += 3
        win_lose_board.append('A')

    elif A[i] < B[i]:
        B_score += 3
        win_lose_board.append('B')
    
    elif A[i] == B[i]:
        A_score += 1
        B_score += 1

if A_score > B_score:
    winner = 'A'

elif A_score < B_score:
    winner = 'B'

elif A_score == B_score and A != B:
    winner = win_lose_board[-1]

elif A == B:
    winner = 'D'

print(A_score, B_score)
print(winner)

