import sys
collect = ['a','e','i','o','u','A','E','I','O','U']
while True:
    lst = list(sys.stdin.readline().rstrip('\n'))
    
    if lst == ['#']:
        break
    
    cnt = 0
    for x in lst:
        if x in collect: 
            cnt += 1
    
    print(cnt)
