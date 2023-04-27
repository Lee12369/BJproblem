T = int(input())
for _ in range(T):
    word = input()
    alphabet = [0 for _ in range(26)]
    for x in word:
        alphabet[ord(x) - 65] += 1
    
    score = 0
    for idx, val in enumerate(alphabet):
        if val == 0:
            score += idx + 65
    
    print(score)