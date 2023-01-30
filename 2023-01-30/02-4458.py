N = int(input())

for _ in range(N):
    sentence = input()

    sentence = sentence[0].upper() + sentence[1:]

    print(sentence)
