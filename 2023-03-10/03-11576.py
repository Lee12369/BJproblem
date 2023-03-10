A, B = map(int, input().split())
N = input()
num_A = list(map(int,input().split()))
num_A.reverse()

num_10 = 0
for idx, val in enumerate(num_A):
    num_10 += val * (A ** idx)

num_B = []
i = 0
while True:
    remain = (num_10 % (B ** (i + 1)))
    dg = remain // (B ** i) 
    num_B.append(dg)
    i += 1

    if remain == num_10:
        break

num_B.reverse()
for x in num_B:
    print(x, end=' ')