team_olym = list(map(int, input().split()))
team_start = list(map(int, input().split()))

olym_score = 0
start_score = 0

gap_score = [0]
check = 0
for i in range(9):
    olym_score += team_olym[i]
    gap = olym_score - start_score
    gap_score.append(gap)
    
    if gap > 0:
        check = 1

    start_score += team_start[i]
    gap = olym_score - start_score
    gap_score.append(gap)
    
if check == 1:
    print('Yes')

else:
    print('No')