word = input()

size = word.count('b')
length = len(word)
pre = word[-size:]
b_cnt = pre.count('b')
max_b_cnt = b_cnt

for i in range(length):
    curr = pre[1:] + word[i]
    if pre[0] == 'b':
        b_cnt -= 1
    if word[i] == 'b':
        b_cnt += 1

    max_b_cnt = max(max_b_cnt, b_cnt)
    pre = curr

answer = size - max_b_cnt

print(answer)