remove_word = [x for x in 'CAMBRIDGE']

word = list(input())
ans = [y for y in word if y not in remove_word]

for x in ans:
    print(x, end='')