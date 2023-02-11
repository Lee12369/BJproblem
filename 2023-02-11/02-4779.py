def recurrsion(word):
    len_word = len(word)
    if len_word <= 1:
        return word
    
    start = len_word // 3
    end = start * 2

    left = word[:start]
    mid = ' ' * (end-start)
    right = word[end:]

    return recurrsion(left) + mid + recurrsion(right)
while True:
    try:
        N = int(input())
        
        word = '-' * (3 ** N)
        answer = recurrsion(word)
        
        print(answer)
    except:
        break
