import sys

def get_cnt(arr, i):
    cnt = 0
    j = 0
    curr = -1
    while j  < N:
        while j < N and arr[i][j] != 'X':
            j += 1
    
        if j - curr >= 3:
            cnt += 1

        curr = j
        j += 1

    return cnt

input = sys.stdin.readline
N = int(input())
arr_rows = [list(input().rstrip('\n')) for _ in range(N)]
arr_columns = list(map(list, zip(*arr_rows)))

row_cnt = 0
column_cnt = 0

for i in range(N):
    row_cnt += get_cnt(arr_rows,i)
    column_cnt += get_cnt(arr_columns,i)    
    
print(row_cnt, column_cnt)

# arr_rows = [['.','.','.','.','X'],['.','.','X','X','.'],['.','.','.','.','.'],['.','X','X','.','.'],['X','.','.','.','.']]
