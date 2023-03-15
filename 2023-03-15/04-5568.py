N = int(input())
K = int(input())
nums = [input() for _ in range(N)]


word = ''
cnt = 0
visited = [0 for _ in range(N)]
ans_lst = []

def back_tracking(word, cnt, visited):
    if cnt == K:
        ans_lst.append(word)
        return 0
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            save_word = word + nums[i]
            save_cnt = cnt + 1
            
            back_tracking(save_word, save_cnt, visited)

            visited[i] = 0

back_tracking(word, cnt, visited)

ans_lst = dict.fromkeys(ans_lst)

ans = len(ans_lst)

print(ans)