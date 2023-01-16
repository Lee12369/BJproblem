N = 3
lst = [list(map(int,input().split())) for _ in range(N)]
x_list = [lst[i][0] for i in range(N)]
y_list = [lst[i][1] for i in range(N)]

for x in x_list:
    if x_list.count(x) == 1:
        x_ans = x
        break
for y in y_list:
    if y_list.count(y) == 1:
        y_ans = y
        break

print("{} {}".format(x_ans,y_ans))

