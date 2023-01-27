import sys
input = sys.stdin.readline
prize_2017 = [500, 300, 200, 50, 30, 10]

number_2017 = []
for i in range(1, 7):
    for _ in range(i):
        number_2017.append(i)

prize_2018 = [int(512 /(2 ** i)) for i in range(5)]

number_2018 = []
for i in range(1, 6):
    M = 2 ** (i - 1)
    for _ in range(M):
        number_2018.append(i)

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    len_num_2017 = len(number_2017)
    len_num_2018 = len(number_2018)

    if 0 < a <= len_num_2017:
        prize_1st = prize_2017[number_2017[a - 1] - 1]
    else:
        prize_1st = 0
    
    if 0 < b <= len_num_2018:
        prize_2nd = prize_2018[number_2018[b - 1] - 1]
    else:
        prize_2nd = 0

    prize_total = (prize_1st + prize_2nd) * 10000
    
    print(prize_total)
    