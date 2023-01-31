N, M = map(int, input().split())

if N >= 7 and M >= 7:
    visit = min(N, M) -7 + 5

elif N < 3 and M < 3:
    visit = 1

elif N == 2:
    if M >= 7:
        visit = 4
    
    elif M >= 5:
        visit = 3

    else:
        visit = 2

elif N >= 3: 
    visit = M

    if visit > 4:
        visit = 4

elif M >= 3:
    visit = M

    if visit > 4:
        visit = 4

else:
    visit = 4

print(visit)

