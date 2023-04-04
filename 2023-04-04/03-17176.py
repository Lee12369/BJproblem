from collections import defaultdict
N = int(input())
nums = list(map(int, input().split()))
password = input()

dic_word = defaultdict(int)
for num in nums:
    if num == 0:
        word = ' '
    
    elif num < 27:
        word = chr(num + 64)
    
    else:
        word = chr(num + 70)

    dic_word[word] += 1

dic_password = defaultdict(int)
for x in password:
    dic_password[x] += 1

if dic_word == dic_password:
    print('y')
else:
    print('n')