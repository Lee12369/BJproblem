# 값이 어마어마하게 크기 때문에 실제 값을 구하기 보다는 리스트에 자리별로 인덱스를 활용한다.
# 개수가 많다고 바꿨을 때 큰 것은 아니다. 예를 들어 Y가 5개 있어도 A를 Z로 바꾸는 것이 더 이득이다.
# 입력은 50이지만 출력은 50보다 클 수 있다.
from collections import defaultdict
import sys
input = sys.stdin.readline

# Z로 변환시 추가적으로 얻을 수 있는 값
def get_gap(dic_cnt, gap):
    for key, val in dic_cnt.items():
        for i in range(1, 53):
            cnt = val[-i]
            gap[key][-i] = (dic['Z'] - dic[key]) * cnt
    
    # 36보다 크면 앞 자리 수를 올려준다.     
    for key, val in dic_cnt.items():
        for i in range(1, 52):
            gap[key][-i -1] += gap[key][-i] // 36
            gap[key][-i] %= 36

# 값이 큰 순서대로 K개를 얻는다.
def get_change_Z(gap):
    change_info = list(gap.values())
    change_info.sort(reverse=True)
    return change_info[:K]

dic = {}
dic_cnt = {}
dic_rev = {}
gap = {}
# 0 ~ 9
for i in range(10):
    dic[str(i)] = i
    dic_cnt[str(i)] = [0 for _ in range(52)]
    dic_rev[i] = str(i)
    gap[str(i)] = [0 for _ in range(52)]
# 10 ~ 35
for i in range(10, 36):
    dic[chr(55 + i)] = i
    dic_cnt[chr(55 + i)] = [0 for _ in range(52)]
    dic_rev[i] = chr(55 + i)
    gap[chr(55 + i)] = [0 for _ in range(52)]

N = int(input())
words = [list(input().rstrip()) for _ in range(N)]
K = int(input())

for word in words:
    W = len(word)
    for number in word:
        dic_cnt[number][-W] += 1
        W -= 1

get_gap(dic_cnt, gap)
change_info = get_change_Z(gap)
for info in change_info:
    for key, val in gap.items():
        # 변화할 값과 정보가 일치하면
        if val == info:
            if key == 'Z':
                continue
            # Z에 개수를 추가한다.
            for i in range(52):
                dic_cnt['Z'][i] += dic_cnt[key][i]
       
            dic_cnt[key] = [0 for _ in range(52)]
            gap[key] = False
            break

# 전체의 합을 구한다.
answer = []
share = 0
for i in range(1, 52):
    num = share
    for key, val in dic_cnt.items():
        num += val[-i] * dic[key]
    answer.append(num % 36)
    share = num // 36
answer.append(share % 36)
answer.append(share // 36)
answer = answer[::-1]

# 36진수에 맞게 변환
ans = ''
for number in answer:
    # 앞자리 0은 생략
    if number == 0 and ans == '':
        continue
    ans += dic_rev[number]

# 만약 전부 0이라 얻어지는 값이 없다면 0
if ans == '':
    ans = 0
print(ans)
