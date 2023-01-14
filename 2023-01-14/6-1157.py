word = str(input()).upper()
visited = []
numlst = []
for i in word:
    if i not in visited:
        visited.append(i)
        numlst.append(word.count(i))

max_num = max(numlst)

if numlst.count(max_num) == 1:
    print(visited[numlst.index(max_num)])
else:
    print('?')
