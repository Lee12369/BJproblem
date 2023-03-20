S = input()
T = input()

cnt = len(T) - len(S)
ans_lst = []
def back_tracking(word, cnt):
    if cnt == 0:
        if word == S:
            ans_lst.append(word)
        return
    
    # 답이 존재할 경우 나머지 종료.
    if ans_lst:
        return
    
    if word[-1] == 'A':
        case1_save_word = word[:-1]
        save_cnt = cnt- 1
        back_tracking(case1_save_word, save_cnt)

    if word[0] == 'B':
        temp = word[-1::-1]
        case2_save_word = temp[:-1]
        save_cnt = cnt - 1
        back_tracking(case2_save_word, save_cnt)

back_tracking(T, cnt)

if ans_lst:
    print(1)
else:
    print(0)
    