import sys
input = sys.stdin.readline

T = int(input())
dic = {
    1:1,
    2:2,
    3:4
}

for x in range(4, 11):
    dic[x] = dic[x - 1] + dic[x - 2] + dic[x - 3]

for _ in range(T):
    N = int(input())
    
    ans = dic[N]

    print(ans)