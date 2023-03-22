import sys
input = sys.stdin.readline

N = int(input())
students_number = [input().rstrip() for _ in range(N)]

len_number = len(students_number[0])

for i in range(1, len_number + 1):
    dic = {}
    for num in students_number:
        dic[num[-i:]] = 1
    
    if len(list(dic.keys())) == len(students_number):
        print(i)
        break
