import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total_score = 0
for i in range(N):
    total_score += sum(arr[i])

lst = []
start_score = 0
lst_ans = []
def back_tracking(start, start_score, lst):
    if len(lst) == N // 2:
        team_link = []
        for i in range(N):
            if i not in lst:
                team_link.append(i)
        
        link_score = 0
        for x in team_link:
            for y in team_link:
                link_score += arr[x][y]

        ans = abs(link_score - start_score)
        lst_ans.append(ans)
        return 0
    
    for i in range(start, N):
        lst.append(i)
        temp = 0
        for x in lst:
            temp += arr[x][i] + arr[i][x]
        start_score += temp

        back_tracking(i + 1, start_score, lst)

        lst.pop()
        start_score -= temp

back_tracking(0, start_score, lst)

print(min(lst_ans))