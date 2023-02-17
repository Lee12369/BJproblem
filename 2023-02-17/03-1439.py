# 구간의 개수에 따라 뒤집는 횟수가 결정됨.
S = input()

pre = S[0]
cnt = 1
for x in S:
    if x != pre:
        cnt += 1
    pre = x

ans = cnt // 2

print(ans)