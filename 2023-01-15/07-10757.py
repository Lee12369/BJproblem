A, B = input().split()
A_list = [0 for i in range(10005)]
B_list = [0 for i in range(10005)]
for i, j in enumerate(A):
    A_list[i + 10005 - len(A)] = int(A[i])
for i, j in enumerate(B):
    B_list[i + 10005 - len(B)] = int(B[i])

answer_list = [0 for i in range(10005)]
for i in range(10005):
    answer_list[-i] = A_list[-i]+B_list[-i]
    if answer_list[-i] >= 10:
        answer_list[-i] -= 10
        A_list[-i-1] += 1

answer = ''
for i in answer_list:
    answer += str(i)
print(int(answer))