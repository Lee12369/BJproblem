N, new_score, P = map(int, input().split())

if N > 0:
    scores = list(map(int, input().split()))
    
    i = 0
    while i < N and new_score < scores[i]:
        i += 1
    rank = i + 1
    if rank > P:
        rank = -1
    elif rank == P and new_score == scores[i]:
        rank = -1
else:
    rank = 1

print(rank)