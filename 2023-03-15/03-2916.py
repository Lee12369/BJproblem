import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

sour = 1
bitter = 0
ans_lst = []
check = 0
def back_tracking(start, sour, bitter, check):
    if check > 0:
        gap = abs(sour - bitter)
        ans_lst.append(gap)
        
    for i in range(start, N):
        save_sour = sour * arr[i][0]
        save_bitter = bitter + arr[i][1]
        check = 1
        back_tracking(i + 1, save_sour, save_bitter, check)

back_tracking(0, sour, bitter, check)

ans = min(ans_lst)

print(ans)