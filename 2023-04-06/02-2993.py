word = input()

lst_word = []
N = len(word)
for i in range(1, N - 2):
    for j in range(i + 1, N):
        word_1 = word[: i]
        word_2 = word[i : j]
        word_3 = word[j :]

        new_word = word_1[::-1] + word_2[::-1] + word_3[::-1]
        lst_word.append(new_word)

lst_word.sort()
print(lst_word[0])