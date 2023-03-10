from collections import defaultdict
import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

Time = 0
N = 3
M = 3
while True:
    if N >= R and M >= C:
        if arr[R - 1][C - 1] == K:
            break
    if Time == 101:
        break
    
    max_cnt = 0
    arr_temp = [[] for _ in range(max(N, M))]
    # R 연산
    if N >= M:
        for i in range(N):
            dic = defaultdict(int)
            cnt = 0
            # 숫자별 개수 파악
            for j in range(M):
                if arr[i][j] > 0:
                    dic[arr[i][j]] += 1
            
            # 개수에 따라 숫자 정렬
            lst_temp = list(dic.items())
            lst_temp.sort(key=lambda x : (x[1], x[0]))
            for tpl in lst_temp:
                x, y = tpl
                arr_temp[i].append(x)
                arr_temp[i].append(y) 
                cnt += 2
            max_cnt = max(max_cnt, cnt)
        
        # 0 추가
        for k in range(N):
            cnt_0 = max_cnt - len(arr_temp[k])
            for _ in range(cnt_0):
                arr_temp[k].append(0)
        
        M = max_cnt
        arr = arr_temp
            
    # C 연산
    else:
        for j in range(M):
            dic = defaultdict(int)
            cnt = 0
            # 숫자별 개수 파악
            for i in range(N):
                if arr[i][j] > 0:
                    dic[arr[i][j]] += 1

            # 개수에 따라 숫자 정렬
            lst_temp = list(dic.items())
            lst_temp.sort(key=lambda x : (x[1], x[0]))
            for tpl in lst_temp:
                x, y = tpl
                arr_temp[j].append(x)
                arr_temp[j].append(y) 
                cnt += 2
            max_cnt = max(max_cnt, cnt)

        # 0 추가
        for k in range(M):
            cnt_0 = max_cnt - len(arr_temp[k])
            for _ in range(cnt_0):
                arr_temp[k].append(0)
        
        N = max_cnt
        arr = list(map(list, zip(*arr_temp)))

    Time += 1

if Time < 101:
    print(Time)
else:
    print(-1)
