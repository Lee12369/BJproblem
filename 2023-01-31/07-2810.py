N = int(input())
M = input()

cnt_LL = M.count('L') // 2

cup_holder = N + 1 - cnt_LL

if N >= cup_holder:
    print(cup_holder)

else:
    print(N)