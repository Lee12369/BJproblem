import sys
N = int(input())
lst = []
for i in range(N):
    number = int(sys.stdin.readline())
    if number != 0:
        lst.append(number)
    else:
        lst.pop()
answer = 0
for i in lst:
    answer += i
print(answer)