word = list(input())
len_word = len(word)

for i in range(len_word):
    if word[i].isupper():
        word[i] = word[i].lower()
    else:
        word[i] = word[i].upper()

for x in word:
    print(x, end='')