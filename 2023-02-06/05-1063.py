king, stone, N = input().split()
N = int(N)

king_x = ord(king[0]) - 64
king_y = int(king[1])

stone_x = ord(stone[0]) - 64
stone_y = int(stone[1])

for _ in range(N):
    move = input()
 
    save = [king_x, king_y]

    if move == 'R':
        if king_x != 8:
            king_x += 1
        if king_x == stone_x and king_y == stone_y:
            if stone_x != 8:
                stone_x += 1

    elif move == 'L':
        if king_x != 1:
            king_x -= 1
        if king_x == stone_x and king_y == stone_y: 
            if stone_x != 1:
                stone_x -= 1

    elif move == 'B': 
        if king_y != 1:
            king_y -= 1
        if king_x == stone_x and king_y == stone_y:
            if stone_y != 1:
                stone_y -= 1

    elif move == 'T':  
        if king_y != 8:        
            king_y += 1
        if king_x == stone_x and king_y == stone_y: 
            if stone_y != 8:
                stone_y += 1
        
    elif move == 'RT':
        if king_x != 8 and king_y != 8: 
            king_x += 1
            king_y += 1
        if king_x == stone_x and king_y == stone_y:
            if stone_x != 8 and stone_y != 8: 
                stone_x += 1
                stone_y += 1
        
    elif move == 'LT': 
        if king_x != 1 and king_y != 8:
            king_x -= 1
            king_y += 1
        if king_x == stone_x and king_y == stone_y:
            if stone_x != 1 and stone_y != 8:
                stone_x -= 1
                stone_y += 1
        
    elif move == 'RB':
        if king_x != 8 and king_y != 1:    
            king_x += 1
            king_y -= 1
        if king_x == stone_x and king_y == stone_y:
            if stone_x != 8 and stone_y != 1:
                stone_x += 1
                stone_y -= 1
        
    elif move == 'LB':
        if king_x != 1 and king_y != 1:    
            king_x -= 1
            king_y -= 1
        if king_x == stone_x and king_y == stone_y: 
            if stone_x != 1 and stone_y != 1:
                stone_x -= 1
                stone_y -= 1
          
    if king_x == stone_x and king_y == stone_y:
        king_x = save[0]
        king_y = save[1]

king_x = chr(king_x + 64)
stone_x = chr(stone_x + 64)

print("{}{}".format(king_x, king_y))
print("{}{}".format(stone_x, stone_y))
