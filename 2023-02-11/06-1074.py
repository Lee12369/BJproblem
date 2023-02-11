def recurr(r, c, start_r, end_r, start_c, end_c, score_start, N):
    if N == 1:
        return score_start

    mid_r = (end_r - start_r) // 2 + start_r
    mid_c = (end_c - start_c) // 2 + start_c
    
    M = N ** 2 // 4
    
    if r < mid_r and c < mid_c:
        end_r = mid_r
        end_c = mid_c
        score_start = score_start 
    
    elif r < mid_r and c >= mid_c:
        end_r = mid_r
        start_c = mid_c
        score_start += M

    elif r >= mid_r and c < mid_c:
        start_r = mid_r
        end_c = mid_c
        score_start += M * 2
    
    elif r >= mid_r and c >= mid_c:
        start_r = mid_r
        start_c = mid_c
        score_start += M * 3
    
    N //= 2
    return recurr(r, c, start_r, end_r, start_c, end_c, score_start, N)
    
N, r, c = map(int, input().split())
M = 2 ** N

answer = recurr(r, c, 0, M, 0, M, 0, M)

print(answer)
