N = int(input())
words = [input() for _ in range(N)]


for i in range(N):
    print("{}. {}".format(i + 1, words[i]))