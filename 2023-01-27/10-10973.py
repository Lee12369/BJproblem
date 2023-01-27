N = int(input())
lst = list(map(int, input().split()))

def get_change():
    change_num = min(lst)
    for x in b:
        if x < lst[-i]:
            change_num = max(change_num, x)

    return change_num

cnt = 0
for i in range(2, N + 1):
    b = sorted(lst[-i:])
    if lst[-i:] != b:

        lst[-i] = get_change()
        
        b.remove(lst[-i])
        b_rev = sorted(b, reverse=True)
        lst[-i + 1:] = b_rev
        cnt = 1
        break

if cnt:
    for x in lst:
        print(x, end=' ')

else:
    print(-1)
