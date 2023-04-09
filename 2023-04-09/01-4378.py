keyboard = ['`','1','2','3','4','5','6','7','8','9','0','-','=','Q','W','E','R','T','Y','U','I','O','P','[',']','\\','A','S','D','F','G','H','J','K','L',';','\'','Z','X','C','V','B','N','M',',','.','/']

# 입력이 여러줄 들어올 수 있고 enter키는 무시
while True:
    try:
        ans = ''
        snt = input()
        for word in snt:
            if word != ' ':
                idx = keyboard.index(word) - 1
                ans += keyboard[idx]
            
            else:
                ans += ' '
        print(ans)
    except:
        break
