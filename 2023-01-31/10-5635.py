N = int(input())
arr = [list(input().split()) for _ in range(N)]

arr.sort(key= lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(arr[-1][0])
print(arr[0][0])
