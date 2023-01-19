word = input()
# print(int(word,16)) 이거 쓰면 바로 끝나긴 함.

dic = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
}

lst = list(str(word))
lst.reverse()
answer = 0

for digit, key in enumerate(lst):

    answer += dic[key] * (16 ** digit)

print(answer)
