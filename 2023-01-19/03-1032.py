N = int(input())
words = [str(input()) for _ in range(N)]

len_word = len(words[0])

for i in range(len_word):
    TF_list = []

    for j in range(N):
        if words[0][i] == words[j][i]:
            TF_list.append(1)
        else:
            TF_list.append(0)

    if 0 not in TF_list:
        print(words[0][i], end='')
    else:
        print('?', end='')