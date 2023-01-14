N = int(input())
for i in range(N):
    reapeat_number, word = input().split() 
    reapeat_number = int(reapeat_number)
    word = str(word)
    for j in word:
        print(j * reapeat_number, end='')
    print()