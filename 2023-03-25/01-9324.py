from collections import defaultdict
T = int(input())
for _ in range(T):
    word = input()
    
    N = len(word)
    check = 0
    dic = defaultdict(int)
    for i in range(N):
        dic[word[i]] += 1
        if dic[word[i]] == 3:
            if i + 1 < N and word[i + 1] == word[i]:
                dic[word[i]] = -1
            else:
                check = 1
                break
    
    if check == 1:
        print("FAKE")
    else:
        print("OK")

        


