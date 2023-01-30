import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    nums = list(map(int, input().rstrip('\n').split()))
    sum_even = 0
    min_even = 100
    for n in nums:
        if n % 2 == 0:
            sum_even += n
            if n < min_even:
                min_even = n 

    print(sum_even, min_even)