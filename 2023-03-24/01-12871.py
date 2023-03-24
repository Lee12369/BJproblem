S = input()
len_S = len(S)

T = input()
len_T = len(T)

def get_word(word, len_word):
    for i in range(1, len_word + 1):
        temp = word[:i]
        N = len_word % i
        M = len_word // i

        if N == 0 and word == temp * M:
            return temp

fs = get_word(S, len_S)
ft = get_word(T, len_T)

if fs == ft:
    print(1)
else:
    print(0)

