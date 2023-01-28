nums = [i for i in range(100,0,-1)]

def selection_sort(lst):
    len_lst = len(lst)
    
    for i in range(len_lst, 0, -1):
        min_idx = lst.index(min(lst[-i:]))
        lst[min_idx], lst[-i] = lst[-i], lst[min_idx]

    return lst

print(selection_sort(nums))
