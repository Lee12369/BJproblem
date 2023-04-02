import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
visited = [0 for _ in range(N)]

cnt = 0
for i in range(N):
    if visited[i] == 0:
        visited[i] = 1
        len_word = len(words[i])
        cnt += 1
        for j in range(i + 1, N):
            for k in range(len_word):
                word = words[i][k:] + words[i][:k]
                if words[j] == word:
                    visited[j] = 1

print(cnt)
