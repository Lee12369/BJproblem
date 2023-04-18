from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    dic = defaultdict(int)

    Ti = nums[0]
    soldiers = nums[1:]
    for soldier in soldiers:
        dic[soldier] += 1
    
    max_cnt = 0
    max_num = 0
    for key, val in dic.items():
        if val > Ti // 2 and val > max_cnt:
            max_num = key
    
    if max_num:
        print(max_num)
    else:
        print('SYJKGW')
        


