word = input()
len_word = len(word)

dp = [0 for _ in range(5001)]
dp[0] = 1
dp[1] = 1
check = 1
for i in range(1, len_word):
    N =  int(word[i - 1] + word[i])
    if N == 0 or (N > 26 and N % 10 == 0):
        check = 0
        break
    
    if N == 10 or N == 20:
        dp[i + 1] = dp[i - 1] % 10 ** 6
        
    elif 11 <= N < 20 or 20 < N <= 26:
        dp[i + 1] = (dp[i] + dp[i - 1]) % 10 ** 6
    
    else:
        dp[i + 1] = dp[i] % 10 ** 6

if check == 0 or len_word == 0 or word[0] == '0':
    ans = 0
else:
    ans = dp[len_word]

print(ans)

