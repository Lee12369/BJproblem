nums = [i for i in range(100,0,-1)]

def selection_sort(lst):
    len_lst = len(lst)
    
    for i in range(len_lst - 1, 1, -1):
        max_idx = lst.index(max(lst[:i + 1]))
        lst[max_idx], lst[i] = lst[i], lst[max_idx]

    return lst

print(selection_sort(nums))
