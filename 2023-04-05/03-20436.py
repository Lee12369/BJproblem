SL, SR = input().split()
words = input()

# 키보드 좌측 좌표
dic_L = {
    'q': (0, 0),
    'w': (0, 1),
    'e': (0, 2),
    'r': (0, 3),
    't': (0, 4),
    'a': (1, 0),
    's': (1, 1),
    'd': (1, 2),
    'f': (1, 3),
    'g': (1, 4),
    'z': (2, 0),
    'x': (2, 1),
    'c': (2, 2),
    'v': (2, 3)
}

# 키보드 우측 좌표
dic_R = {
    'y': (0, 5),
    'u': (0, 6),
    'i': (0, 7),
    'o': (0, 8),
    'p': (0, 9),
    'h': (1, 5),
    'j': (1, 6),
    'k': (1, 7),
    'l': (1, 8),
    'b': (2, 4),
    'n': (2, 5),
    'm': (2, 6)
}


time = 0
for word in words:
    if word in dic_L.keys():
        x1, y1 = dic_L[word]
        x2, y2 = dic_L[SL]
        SL = word
        
    else:
        x1, y1 = dic_R[word]
        x2, y2 = dic_R[SR]
        SR = word
    
    time += abs(x2 - x1) + abs(y2 - y1) + 1

print(time)