from collections import defaultdict
N = int(input())
skill = input()

cnt = 0
dic_skill = defaultdict(int)
for i in range(N):
    # 기본 기술 성공 시
    if skill[i].isnumeric():
        cnt += 1
    
    # 사전 기술 등록
    elif skill[i] == 'L':
        dic_skill['L'] += 1

    elif skill[i] == 'S':
        dic_skill['S'] += 1
    
    # 연계 기술 성공 시
    elif skill[i] == 'R' and dic_skill['L'] > 0:
        cnt += 1
        dic_skill['L'] -=  1
    
    elif  skill[i] == 'K' and dic_skill['S'] > 0:
        cnt += 1
        dic_skill['S'] -= 1

    # 연계 기술 실패 시, 사전 기술 초기화
    else:
        break

print(cnt)
