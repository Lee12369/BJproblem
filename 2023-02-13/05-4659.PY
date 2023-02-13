def check_same_letter(word):
    check = True
    length = len(word)
    for i in range(length - 1):
        if word[i] == word[i + 1]:
            if word[i] != 'e' and word[i] != 'o':
                check = False

    return check

def check_three_letter(word):
    check = True
    length = len(word)
    for i in range(length - 2):
        lst = [word[i], word[i + 1], word[i + 2]]
        cnt = 0
        for x in lst:
            if x in vowel:
                cnt += 1
        if cnt == 0 or cnt == 3:
            check = False
    
    return check

def check_in_vowel(word):
    check = False
    for x in word:
        if x in vowel:
            check = True
            break
    return check

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()
    if word == 'end':
        break
    check_1 = check_same_letter(word)
    check_2 = check_three_letter(word)
    check_3 = check_in_vowel(word)

    if check_1 == True and check_2 == True and check_3 == True:
        print("<{}> is acceptable.".format(word))
    else:
        print("<{}> is not acceptable.".format(word))
        
