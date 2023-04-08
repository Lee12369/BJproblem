import sys
input = sys.stdin.readline

N = int(input())
cnt_words = 0
arr_sentences = []
for _ in range(N):
    sentence = list(input().split())
    arr_sentences.append(sentence)
    cnt_words += len(sentence)

all_sentence = list(input().split())

for word in all_sentence:
    check = "Impossible"
    for i in range(N):
        if arr_sentences[i] and word == arr_sentences[i][0]:
            check = "Possible"
            arr_sentences[i] = arr_sentences[i][1:]
            break
        
    if check == "Impossible":
        break

# 앵무새가 부른 단어의 개수가 부족하거나 많으면 Impossible이다. 
if cnt_words != len(all_sentence):
    check = "Impossible"

print(check)