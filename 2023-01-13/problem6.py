# 별 찍기
num = int(input(''))
for i in range(1,num+1):
    for j in range(i):
        print('*', end='')
    print()