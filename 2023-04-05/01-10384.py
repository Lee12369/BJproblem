from collections import defaultdict

case = 1
T = int(input())
for _ in range(T):
    word = input().upper()
    dic = defaultdict(int)
    for x in word:
        if 65 <= ord(x) <= 90:
            dic[x] += 1
    
    if len(dic) < 26:
        print("Case {}: Not a pangram".format(case))
    
    elif min(dic.values()) == 1:
        print("Case {}: Pangram!".format(case))
    
    elif min(dic.values()) == 2:
        print("Case {}: Double pangram!!".format(case))
    
    elif min(dic.values()) == 3:
        print("Case {}: Triple pangram!!!".format(case))
    
    case += 1

    

    