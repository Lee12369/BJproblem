cnt = 0
answer = []
for i in range(5):
    code_name = input().split('-')
    for x in code_name:
        if 'FBI' in x:
            answer.append(i + 1)
            cnt += 1
    
if cnt:
    for x in answer:
        print(x, end=' ')
else:
    print("HE GOT AWAY!")
