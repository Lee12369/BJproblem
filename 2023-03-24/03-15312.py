dic = {
    'A' : 3,
    'B' : 2,
    'C' : 1,
    'D' : 2,
    'E' : 3,

    'F' : 3,
    'G' : 2,
    'H' : 3,
    'I' : 3,
    'J' : 2,

    'K' : 2,
    'L' : 1,
    'M' : 2,
    'N' : 2,
    'O' : 1,

    'P' : 2,
    'Q' : 2,
    'R' : 2,
    'S' : 1,
    'T' : 2,

    'U' : 1,
    'V' : 1,
    'W' : 1,
    'X' : 2,
    'Y' : 2,

    'Z' : 1
}

word_A = input()
word_B = input()

N = len(word_A)

dp = []
for i in range(N):
    dp.append(dic[word_A[i]])
    dp.append(dic[word_B[i]])

while len(dp) > 2:
    new_dp = []
    for i in range(len(dp) - 1):
        num = (dp[i] + dp[i + 1]) % 10
        new_dp.append(num)
    
    dp = new_dp.copy()

for x in dp:
    print(x, end='')