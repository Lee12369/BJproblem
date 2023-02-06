import sys
input = sys.stdin.readline 
T = int(input())
for t in range(T):
    lst = list(map(int, input().rstrip('\n').split()))
    N = lst[0]
    grades = lst[1:]
    grades.sort()
    min_grade = grades[0]
    max_grade = grades[-1]

    max_gap = 0
    for i in range(N - 1):
        gap = grades[i + 1] - grades[i]
        max_gap = max(gap, max_gap)
    
    print("Class {}".format(t + 1))
    print("Max {}, Min {}, Largest gap {}".format(max_grade, min_grade, max_gap))