N = int(input())
ans = 0
for i in range(N):
    word = input()
    pre = word[0]
    visited = [word[0]]
    for curr in word:
        if curr != pre:
            if curr not in visited:
                visited.append(curr)
            else: 
                visited.append('False')
                break
        elif curr == pre:
            pass
        # elif curr in visited:    
        pre = curr 
    if 'False' not in visited: 
        ans +=1
print(ans)