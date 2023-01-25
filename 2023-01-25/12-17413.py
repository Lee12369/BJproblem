import sys
word_lists = list(sys.stdin.readline().rstrip('\n'))

start = 0
i = 0
while i < len(word_lists):
    if word_lists[i] == '<':
        while word_lists[i] != '>':
            i += 1
        i += 1

    elif word_lists[i].isalnum():
        start = i
        while i < len(word_lists) and word_lists[i].isalnum():
            i += 1
        temp = word_lists[start:i]
        temp.reverse()
        word_lists[start:i] = temp

    else:
        i += 1
        
for x in word_lists:
    print(x, end='')    
