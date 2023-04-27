N, P = map(int, input().split())

nums = []
curr = N
cnt = 0
while True:
    curr = curr * N % P
    if curr not in nums:
        nums.append(curr)
        cnt += 1
    else:
        # 전체 개수에서 반복이 시작되는 위치를 빼면 반복되는 구간의 개수를 얻을 수 있다.
        ans = cnt - nums.index(curr)
        print(ans)
        break

