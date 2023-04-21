L = int(input())
word = input()

ans = 0
multiple_num = 1
for i in range(L):
    ans += ((ord(word[i]) - 96) * multiple_num) % 1234567891
    multiple_num *= 31

ans = ans % 1234567891

print(ans)