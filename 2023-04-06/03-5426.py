import math

T = int(input())
for _ in range(T):
    word = input()

    N = len(word)
    M = int(math.sqrt(N))

    # 단어를 배열 형태로 정렬
    arr = []
    for i in range(M):
        start = i * M
        end = (i + 1) * M
        arr.append(word[start : end])

    # 순서는 오른쪽 위를 시작으로 가장 아래까지. 그 다음 옆으로 이동해 가장 아래까지. 
    # 이를 반복해 단어를 읽어 암호를 해독한다.
    ans = ''
    for j in range(M - 1, -1, -1):
        for i in range(M):
            ans += arr[i][j]
    
    print(ans)