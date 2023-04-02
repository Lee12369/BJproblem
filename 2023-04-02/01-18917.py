import sys
input = sys.stdin.readline

nums = [0]
M = int(input())
calc_3 = 0
calc_4 = 0
for _ in range(M):
    num1, *num2 = map(int, input().split())
    if num1 == 1:
        calc_3 += num2[0]
        calc_4 ^= num2[0]

    elif num1 == 2:
        calc_3 -= num2[0]
        calc_4 ^= num2[0]

    elif num1 == 3:
        print(calc_3)
    
    elif num1 == 4:
        print(calc_4)