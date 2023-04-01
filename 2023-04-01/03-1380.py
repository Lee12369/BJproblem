case = 1
while True:
    N = int(input())
    if N == 0:
        break

    lst_names = [""] 
    for _ in range(N):
        name = input()
        lst_names.append(name)

    # 인덱스의 등장 횟수만큼 더해준다. 값이 1일 경우, 그 사람이 귀걸이를 돌려받지 못한 여학생이 된다.
    cnt = [0 for _ in range(N + 1)]
    for _ in range(2 * N - 1):
        num, _ = input().split()
        cnt[int(num)] += 1
    
    idx = cnt.index(1)
    print("{} {}".format(case, lst_names[idx]))
    
    case += 1