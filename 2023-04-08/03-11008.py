T = int(input())
for _ in range(T):
    s, p = input().split()
    
    len_s = len(s)
    len_p = len(p)

    cnt = 0
    curr = 0
    while curr < len_s:
        if p == s[curr: curr + len_p]:
            curr += len_p
        else:
            curr += 1
        
        cnt += 1
    
    print(cnt)