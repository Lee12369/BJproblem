N, K = map(int, input().split())

nums = [1,2,3]

score = 0
score_lst = []
ans_lst = []
def back_tracking(score, score_lst):
    if score == N:
        ans_lst.append(score_lst)
        return 0
    
    if score > N:
        return 0
    
    for i in range(3):
        save_score = score + nums[i]
        save_score_lst = score_lst + [nums[i]]

        back_tracking(save_score, save_score_lst)

back_tracking(score, score_lst)

if K <= len(ans_lst):
    M = len(ans_lst[K - 1])
    for i in range(M - 1):
        print(ans_lst[K - 1][i], end='+')
    print(ans_lst[K - 1][-1])

else:
    print(-1)