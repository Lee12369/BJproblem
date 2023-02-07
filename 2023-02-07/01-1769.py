X = list(map(int, input()))
if len(X) > 1:
    cnt = 1
else:
    cnt = 0

X_num = sum(X)
while X_num > 9:
    temp = list(map(int, str(X_num)))
    X_num = sum(temp)
    cnt += 1

print(cnt)
if X_num % 3 == 0:
    print("YES")
else:
    print("NO")