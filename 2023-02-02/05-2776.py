import sys
input = sys.stdin.readline

def in_check(note, N, x):
    left = 0
    right = N - 1
    while True:
        mid = (left + right) // 2
        mid_nums = note[mid]

        if mid == left:
            if note[left] != x and note[right] != x:
                return 0
            else:
                return 1

        if x == mid_nums:
            return 1
            
        elif x > mid_nums:
            left = mid
        elif x < mid_nums:
            right = mid
    


T = int(input())
for _ in range(T):
    N = int(input())
    note = list(map(int, input().rstrip('\n').split()))
    note.sort()
    M = int(input())
    nums = list(map(int, input().rstrip('\n').split()))

    
    for x in nums:
        answer = in_check(note, N, x)
        print(answer)