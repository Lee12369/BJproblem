Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r','s','t','u','v','w','x','y','z']
# Alphabet = [chr(i) for i in range(97,123)]
print(Alphabet)
S = list(str(input()))
for i in Alphabet:
    if i not in S:
        Answer = -1
    else:
        for j in range(len(S)):
            if i == S[j]:
                Answer = j
                break
    print(Answer, end=' ')