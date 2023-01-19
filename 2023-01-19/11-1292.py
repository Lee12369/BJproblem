A, B = map(int,input().split())
list_numbers =[]

for i in range(1, 46):
    for _ in range(i):
        list_numbers.append(i)

answer = 0
for j in range(A - 1, B):
    answer += list_numbers[j]

print(answer)