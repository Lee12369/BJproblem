A = list(map(int, input().split()))
B = list(map(int, input().split()))

win_lose_board = []

for i in range(10):
    if A[i] > B[i]:
        win_lose_board.append('A')
    
    elif A[i] < B[i]:
        win_lose_board.append('B')
    
    elif A[i] == B[i]:
        win_lose_board.append('D')

cnt_A = win_lose_board.count('A')
cnt_B = win_lose_board.count('B')

if cnt_A > cnt_B:
    print('A')

elif cnt_A < cnt_B:
    print('B')
    
elif cnt_A == cnt_B:
    print('D')
    