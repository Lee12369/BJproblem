N = int(input())

M = 4 * (N - 1) + 1

arr = [[' ' for _ in range(M)] for _ in range(M)]

start = 0 
end = M
    
while M > 0:
    for i in range(start, end):
        if i == start or i == end - 1:
            for j in range(start, end):
                arr[i][j] = '*'
        else:
            arr[i][start] = '*'
            arr[i][end - 1] = '*'
        
    M -= 4
    start += 2
    end -= 2

for lst in arr:
    for x in lst:
        print(x, end='')
    print()          
            