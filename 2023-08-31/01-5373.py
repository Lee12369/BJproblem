from collections import deque
import sys
input = sys.stdin.readline

class Cube:
    def __init__(self, up, down, front, back, left, right) -> None:
        self.up = up
        self.down = down
        self.front = front
        self.back = back
        self.left = left
        self.right = right

def clockwise(plane):
    plane = [[row[i] for row in plane[::-1]] for i in range(3)]
    return plane

def counterclockwise(plane):
    plane = [[row[-i - 1] for row in plane] for i in range(3)]
    return plane

def get_column(plane, number):
    column = []
    for row in plane:
        column.append(row[number])    
    return column

def up(cube, sign):
    cube.up = rotate_main[sign](cube.up)

    back, right, front, left = cube.back[0][::-1], cube.right[0][::-1], cube.front[0][::-1], cube.left[0][::-1]
    
    queue = deque([back, right, front, left])
    queue.rotate(rotate_other[sign])
    back, right, front, left = queue
    cube.back[0] = back[::-1]
    cube.right[0] = right[::-1]
    cube.front[0] = front[::-1]
    cube.left[0] = left[::-1]

def down(cube, sign):
    cube.down = rotate_main[sign](cube.down)

    back, left, front, right = cube.back[2], cube.left[2], cube.front[2], cube.right[2]
    
    queue = deque([back, left, front, right])
    queue.rotate(rotate_other[sign])
    back, left, front, right = queue
    cube.back[2] = back
    cube.left[2] = left
    cube.front[2] = front
    cube.right[2] = right

def front (cube, sign):
    cube.front = rotate_main[sign](cube.front)

    up, right, down, left = cube.up[2], get_column(cube.right, 0), cube.down[2], get_column(cube.left, 2)[::-1]
    queue = deque([up, right, down, left])
    queue.rotate(rotate_other[sign])
    up, right, down, left = queue
    cube.up[2] = up
    cube.right[0][0], cube.right[1][0], cube.right[2][0] = right
    cube.down[2] = down
    cube.left[2][2], cube.left[1][2], cube.left[0][2] = left

def back(cube, sign):
    cube.back = rotate_main[sign](cube.back)

    up, left, down, right = cube.up[0][::-1], get_column(cube.left, 0), cube.down[0][::-1], get_column(cube.right, 2)[::-1]
    queue = deque([up, left, down, right])
    queue.rotate(rotate_other[sign])
    up, left, down, right = queue
    cube.up[0] = up[::-1]
    cube.left[0][0], cube.left[1][0], cube.left[2][0] = left
    cube.down[0] = down[::-1]
    cube.right[2][2], cube.right[1][2], cube.right[0][2] = right
    
def left(cube, sign):
    cube.left = rotate_main[sign](cube.left)
    up, front, down, back = get_column(cube.up, 0), get_column(cube.front, 0), get_column(cube.down, 2)[::-1], get_column(cube.back, 2)[::-1]
    
    queue = deque([up, front, down, back])
    queue.rotate(rotate_other[sign])
    up, front, down, back = queue
   
    cube.up[0][0], cube.up[1][0], cube.up[2][0] = up
    cube.front[0][0], cube.front[1][0], cube.front[2][0] = front
    cube.down[2][2], cube.down[1][2], cube.down[0][2] = down
    cube.back[2][2], cube.back[1][2], cube.back[0][2] = back

def right(cube, sign):
    cube.right = rotate_main[sign](cube.right)

    up, back, down, front = get_column(cube.up, 2)[::-1], get_column(cube.back, 0), get_column(cube.down, 0), get_column(cube.front, 2)[::-1]
    
    queue = deque([up, back, down, front])
    queue.rotate(rotate_other[sign])
    up, back, down, front = queue

    cube.up[2][2], cube.up[1][2], cube.up[0][2] = up
    cube.back[0][0], cube.back[1][0], cube.back[2][0] = back
    cube.down[0][0], cube.down[1][0], cube.down[2][0] = down
    cube.front[2][2], cube.front[1][2], cube.front[0][2] = front
    




rotate_main = {
    '+' : clockwise,
    '-' : counterclockwise
}

rotate_other = {
    '+' : 1,
    '-' : -1
}

commands_dic = {
    'U' : up,
    'D' : down,
    'F' : front,
    'B' : back,
    'L' : left,
    'R' : right
}

T = int(input())
for _ in range(T):
    cube = Cube([['w','w','w'], ['w','w','w'], ['w','w','w']], [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']], [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']])

    n = int(input())
    commands = list(input().split())
    for command in commands:
        alphabet, sign = list(command)
        commands_dic[alphabet](cube, sign)

    answer = cube.up
    for lst in answer:
        for color in lst:
            print(color, end='')
        print()
