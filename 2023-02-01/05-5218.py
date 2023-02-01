T = int(input())

alphabet = [chr(i) for i in range(65,91)]

dic = {val : idx + 1 for idx, val in enumerate(alphabet)}
  
for _ in range(T):
    word_1, word_2 = input().split()
    
    answer = []
    for i in range(len(word_1)):
        ans = dic[word_2[i]] - dic[word_1[i]]
        if ans < 0:
            ans += 26  
        answer.append(ans)
    
    print("Distances: ", end='')
    for x in answer:
        print(x, end=' ')
    print()