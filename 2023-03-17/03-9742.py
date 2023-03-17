import sys
input = sys.stdin.readline

def back_tracking(word, cnt, visited):
    if cnt == M:
        ans_lst.append(word)
        return 0
    
    for i in range(M):
        if visited[i] == 0:
            visited[i] = 1
            save_word = word + word_lst[i]
            save_cnt = cnt + 1

            back_tracking(save_word, save_cnt, visited)

            visited[i] = 0


while True:
    try:
        word_input, N = input().split()
        word_lst = list(word_input)
        N = int(N)
        M = len(word_lst)
        
        cnt = 0
        visited = [0 for _ in range(M)]
        ans_lst = []

        back_tracking('', cnt, visited)

        print("{} {} = ".format(word_input, N), end='')
        if len(ans_lst) >= N:
            print(ans_lst[N - 1])
        else:
            print("No permutation")

    except:
        break
