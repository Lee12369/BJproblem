nums = list(map(int, input().split()))
dic = {}
dic['A'] = min(nums)
dic['C'] = max(nums)

for x in nums:
    if x != dic['A'] and x != dic['C']:
        dic['B'] = x

word = input()

for x in word:
    print(dic[x], end=' ')