T = int(input())

lists = [input() for _ in range(T)]

for lst in lists:
    print("{}{}".format(lst[0], lst[-1]))
