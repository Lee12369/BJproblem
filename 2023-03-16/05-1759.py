L, C = map(int, input().split())

alphabet = list(input().split())
alphabet.sort()

vowel = ['a', 'e', 'i', 'o', 'u']

vowel_cnt = 0
save_lst = []
visited = [0 for _ in range(C)]

def back_tracking(start, vowel_cnt, save_lst, visited):
    if len(save_lst) == L:
        # 모음 1개 이상, 자음 2개 이상으로 구성.
        if vowel_cnt >= 1 and len(save_lst) - vowel_cnt >= 2:
            for x in save_lst:
                print(x, end='')
            print()    
        return 0
    
    for i in range(start, C):
        if visited[i] == 0:
            visited[i] = 1
            save_lst.append(alphabet[i])

            save_vowel_cnt = int(vowel_cnt)
            if alphabet[i] in vowel:
                save_vowel_cnt = vowel_cnt + 1
            
            back_tracking(i + 1, save_vowel_cnt, save_lst, visited)

            visited[i] = 0
            save_lst.pop()

back_tracking(0, vowel_cnt, save_lst, visited)

