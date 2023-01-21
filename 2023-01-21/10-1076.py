dic = {
    'black' : [0, 1],
    'brown' : [1, 10],
    'red' : [2, 100],
    'orange' : [3, 1000],
    'yellow' : [4, 10000],
    'green' : [5, 100000],
    'blue' : [6, 1000000],
    'violet' : [7, 10000000],
    'grey' : [8, 100000000],
    'white' : [9, 1000000000]
}

A, B, C = [input() for _ in range(3)]


first_num = dic[A][0]
second_num = dic[B][0]
zero_num = dic[C][1]

answer = int(str(first_num) + str(second_num)) * zero_num

print(answer)



