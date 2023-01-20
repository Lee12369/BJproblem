N = [int(input()) for _ in range(5)]

average = int(sum(N) / len(N))
median = sorted(N)[2]

print(average)
print(median)
