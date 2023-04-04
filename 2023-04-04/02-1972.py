while True:
    word = input()
    if word == '*':
        break

    N = len(word)
    # N 이 2 이하일 경우 for 문 안으로 들어가지 않고 유일하다. 
    surprising_check = 1
    for i in range(N - 2):
        lst_words = []
        surprising_check = 1
        for j in range(N - i - 1):
            D_word = word[j] + word[j + i + 1]
            lst_words.append(D_word)

        # set 을 이용해 중복을 제거한 이후의 개수가 줄어들었다면 break 한다.
        if len(set(lst_words)) < N - i - 1:
            surprising_check = 0
            break
    
    # 출력(break를 했는지 여부에 따라 출력결과가 달라짐.)
    if surprising_check == 1:
        print("{} is surprising.".format(word))
        
    elif surprising_check == 0:
        print("{} is NOT surprising.".format(word))
        
    
        
        