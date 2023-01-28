nums = [i for i in range(100,0,-1)]

def selection_sort(lst):
    len_lst = len(lst)
    if len_lst <= 1:
        return lst
    pivot = lst[len_lst // 2]
    low_lst, equal_lst, high_lst = [], [], []
    
    for x in lst:
        if x < pivot:
            low_lst.append(x)
        
        elif x > pivot:
            high_lst.append(x)
        
        else:
            equal_lst.append(x)

    return selection_sort(low_lst) + equal_lst + selection_sort(high_lst)

print(selection_sort(nums))