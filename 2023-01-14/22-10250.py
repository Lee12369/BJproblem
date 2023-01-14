n = int(input())
for i in range(n):
    H, W, N = map(int,input().split())
    YY = N % H
    XX = N // H + 1
    if YY == 0:
        XX -= 1 
        YY = H
    if XX < 10:
        XX = '0' + str(XX)
    print("{}{}".format(YY,XX))
