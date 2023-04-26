N, M, L = map(int, input().split())
catch = [0 for _ in range(N + 1)]

curr = 1
catch[1] = 1
while True:
    if catch[curr] == M:
        break
    
    if catch[curr] % 2 == 0:
        curr -= L
    else:
        curr += L

    if curr <= 0:
        curr += N
    elif curr > N:
        curr -= N

    catch[curr] += 1


# 처음 시작할 때는 공을 던진 것이 아니기에 제외한다.
ans = sum(catch) - 1

print(ans)