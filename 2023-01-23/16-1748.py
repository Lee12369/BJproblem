N = int(input())


lst = []
i = 0
while True:
    temp = N - 9 * (10 ** i)
    if temp < 0:
        lst.append(N)
        break
    
    lst.append(9 * (10 ** i))
    
    i += 1
    N = temp

answer = 0
for idx, val in enumerate(lst):
    answer += val * (idx + 1)

print(answer)