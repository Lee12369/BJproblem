N, _ = map(int, input().split())

for _ in range(N):
    word = input()
    print(word[-1::-1])