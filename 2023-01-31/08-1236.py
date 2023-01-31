def get_cnt(arr):
    cnt = 0
    for lst in arr:
        word = ''
        for x in lst:
            word += x
        if 'X' not in word:
            cnt += 1
    
    return cnt

N, M = map(int, input().split())

arr_row = [list(input()) for _ in range(N)]
arr_column = list(map(list, zip(*arr_row)))

cnt_row = get_cnt(arr_row)
cnt_column = get_cnt(arr_column)

answer = max(cnt_row, cnt_column)

print(answer)

