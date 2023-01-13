import sys
iter_num = int(input(''))
Opoint = 0
grade = 0
for i in range(iter_num):
    Answer = list(map(str,sys.stdin.readline()))
    while Answer:
        a = Answer.pop(0)
        if a == 'O':
            Opoint += 1
            grade += Opoint 
        else :
            Opoint = 0
    print(grade)
    grade = 0
