word = input()

# C++ check
if word == word.lower():
    word = word.title()
    word = word[0].lower() + word[1:]
    lst_word = list(word.split('_'))
    if '' not in lst_word:
        ans = ''.join(lst_word)
    else:
        ans = 'Error!'
# java check
elif word[0].islower() and word.isalpha():
    len_word = len(word)
    lst_word = ['']
    for x in word:
        if x.islower():
            lst_word[-1] += x
        else:
            lst_word.append(x.lower())
    
    ans = '_'.join(lst_word)

else:
    ans = 'Error!'

print(ans)


