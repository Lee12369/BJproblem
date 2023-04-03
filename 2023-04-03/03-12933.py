sound = input()

# 'q', 'qu', 'qua', 'quac', 'quack' 의 개수
duck = [0, 0, 0, 0, 0]
word = ['q', 'u', 'a', 'c', 'k']

max_cnt = 0
for x in sound:
    idx = word.index(x)
    if x == 'q':
        duck[idx] += 1

    elif duck[idx - 1] > 0:
        duck[idx] += 1
        duck[idx - 1] -= 1

    else:
        max_cnt = -1
        break

    if duck[-1] == 1:
        cnt = sum(duck)
        max_cnt = max(max_cnt, cnt)
        duck[-1] = 0

# 울음 소리를 끝까지 못 낼 경우.
if sum(duck) > 0:
    max_cnt = -1

print(max_cnt)