import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    idx, word = input().rstrip('\n').split()
    idx = int(idx)
    word = word[:idx-1] + word[idx:]
    print(word)
