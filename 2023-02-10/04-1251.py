word = input()

word_len = len(word)
lst_new_words = []
for slice_1st in range(0, word_len):
    for slice_2nd in range(slice_1st, word_len):
        part1 = word[slice_1st :: -1]
        part2 = word[slice_2nd : slice_1st : -1]
        part3 = word[: slice_2nd : -1]
        if part1 != '' and part2 != '' and part3 != '':
            new_word = part1 + part2 + part3
            lst_new_words.append(new_word)

lst_new_words.sort()

print(lst_new_words[0])
