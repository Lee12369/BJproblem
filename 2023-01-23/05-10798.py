words = [list(input()) for _ in range(5)] 
max_len = len(words[0])

for x in words:
    if len(x) > max_len:
        max_len = len(x)

for x in words:
    while max_len > len(x): 
        x.append('')

answer = ''
for i in range(max_len):
    for j in range(5):
        answer += words[j][i]

print(answer)