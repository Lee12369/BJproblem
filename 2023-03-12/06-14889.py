import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total_score = 0
for i in range(N):
    total_score += sum(arr[i])

lst = []
score = 0
min_ans = int(total_score)
def back_tracking(start, score, lst):
    if len(lst) == N // 2:
        ans = abs(total_score - 2 * score)
        min_ans = min(min_ans, ans)
        return 0
    
    for i in range(start, N):
        lst.append(i)
        temp = 0
        for x in lst:
            temp += arr[x][i] + arr[i][x]
        score += temp

        back_tracking(i + 1, score, lst)

        lst.pop()
        score -= temp

back_tracking(0, score, lst)

print(min_ans)