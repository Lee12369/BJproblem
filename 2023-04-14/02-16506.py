def change_binary(number, digit):
    binary_number = ''
    for i in range(digit - 1, -1, -1):
        binary_number += str(number // (2 ** i))
        number %= 2 ** i

    return binary_number

N = int(input())
words = ['ADD', 'SUB', 'MOV', 'AND', 'OR', 'NOT', 'MULT', 'LSFTL', 'LSFTR', 'ASFTR', 'RL', 'RR']
for _ in range(N):
    robot_word = ''
    opcode, rD, rA, rB = input().split()

    # 0 ~ 4, opcode index 값을 2진수로 바꾼 값 4자리 + 끝에 'C'의 유무에 따른 1자리
    if opcode[-1] == 'C':
        robot_word += change_binary(words.index(opcode[:-1]), 4) + '1'
    else:
        robot_word += change_binary(words.index(opcode), 4) + '0'

    # 5
    robot_word += '0'

    # 6 ~ 8
    robot_word += change_binary(int(rD), 3)

    # 9 ~ 11
    robot_word += change_binary(int(rA), 3)

    # 12 ~ 15
    if robot_word[4] == '0':
        robot_word += change_binary(int(rB), 3) + '0'
    else:
        # rB 로 사용하지 않을 경우 #C 로 사용된다. 즉 #C = rB 이다.
        robot_word += change_binary(int(rB), 4)

    print(robot_word)

