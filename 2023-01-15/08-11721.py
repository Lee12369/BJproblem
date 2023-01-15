word = input()
cnt = 0
for i in word:
    print(i,end='')
    cnt += 1
    if cnt % 10 == 0:
        print()