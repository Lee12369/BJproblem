word = input()

N = len(word)
JOI = 0
IOI = 0
for i in range(N):
    if word[i:i + 3] == 'JOI':
        JOI += 1
    
    elif word[i:i + 3] == 'IOI':
        IOI += 1

print(JOI)
print(IOI)