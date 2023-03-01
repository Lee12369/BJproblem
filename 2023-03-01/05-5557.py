from collections import defaultdict
N = int(input())
nums = list(map(int, input().split()))

pre_dic = defaultdict(int)
pre_dic[nums[0]] = 1

dx = [1, -1]

for i in range(1, N - 1):
    num = nums[i]
    dic = defaultdict(int)
    for key in pre_dic.keys():
        for i in range(2):
            nx = key + num * dx[i]
            if 0 <= nx <= 20:
                dic[nx] += pre_dic[key] 
    pre_dic = dic

ans = dic[nums[-1]]

print(ans)