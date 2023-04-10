N = int(input())
lst = [set() for _ in range(6)]
ans_lst = [set(), {3, 4}, set(), {1, 4}, {1, 3}, set()]
for _ in range(N):
    num1, num2 = map(int, input().split())
    lst[num1].add(num2)
    lst[num2].add(num1)

if lst == ans_lst:
    print("Wa-pa-pa-pa-pa-pa-pow!")

else:
    print("Woof-meow-tweet-squeek")