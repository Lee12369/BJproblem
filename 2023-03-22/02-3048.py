N, M = map(int, input().split())
group1 = input()
group2 = input()
T = int(input())

word = group1[::-1] + group2

group1 = list(group1)
group2 = list(group2)
for _ in range(T):
    temp = str(word)
    for i in range(N + M - 1):
        if temp[i] in group1 and temp[i + 1] in group2:
            word = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        
print(word)