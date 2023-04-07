word = input()
N = len(word)

def get_check(start_num):
    M = str(start_num)
    end_num = start_num
    while True:
        if int(M) == int(word):
            return 1, end_num
        
        elif int(M) > int(word):
            return 0, end_num
            
        start_num += 1
        end_num = start_num
        M += str(start_num)

for i in range(N):
    start_num = int(word[:i + 1])

    check, end_num = get_check(start_num)

    if check == 1:
        print(start_num, end_num)
        break 
   
