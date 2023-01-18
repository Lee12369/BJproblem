dic={
    1 : 'A',
    2 : 'B',
    3 : 'C',
    4 : 'D',
    0 : 'E' 
}

for _ in range(3):
    N = list(map(int,input().split()))
    
    M = N.count(0)
    
    print(dic[M])