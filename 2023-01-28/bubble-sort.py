nums = [i for i in range(100,0,-1)]

def bubble_sort(lst):
    len_lst = len(lst)
    for N in range(len_lst - 1, 0, -1):
        for i in range(N):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    
    return lst 

print(bubble_sort(nums))
