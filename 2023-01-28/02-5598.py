word = list(input())

alphabet = [chr(i) for i in range(65, 91)]

for x in word:
    idx = alphabet.index(x) - 3
    print(alphabet[idx], end='')
    