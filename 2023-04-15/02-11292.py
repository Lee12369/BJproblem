while True:
    N = int(input())
    if N == 0:
        break
    
    name_and_height = []
    for _ in range(N):
        name, height = input().split()
        name_and_height.append((name, float(height)))

    name_and_height.sort(key=lambda x:-x[1])
    max_height = name_and_height[0][1]
    for tpl in name_and_height:
        name, height = tpl
        if height == max_height:
            print(name, end=' ')
        else:
            break
    
    print()
