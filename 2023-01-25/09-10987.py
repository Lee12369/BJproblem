lst = ['a', 'e', 'i', 'o', 'u']

word = list(input())

cnt = 0
for x in word:
    if x in lst:
        cnt += 1

print(cnt)