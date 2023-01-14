x, y = input().split()
x_reverse = ''
y_reverse = ''
for i in range(len(x)):
    x_reverse += x[len(x)-i-1]
for j in range(len(y)):
    y_reverse += y[len(y)-j-1]

x_reverse = int(x_reverse)
y_reverse = int(y_reverse)

if x_reverse > y_reverse:
    print(x_reverse)
elif y_reverse > x_reverse:
    print(y_reverse)  