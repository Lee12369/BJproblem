def mergy(left_lst, right_lst):
    
    sort_lst = []
    i = 0
    j = 0 
    while (i < len(left_lst)) and (j < len(right_lst)):
        if left_lst[i] <= right_lst[j]:
            sort_lst.append(left_lst[i])
            i += 1
        else:
            sort_lst.append(right_lst[j])
            j += 1
    
    if i == len(left_lst):
        sort_lst = sort_lst + right_lst[j:]

    if j == len(left_lst):
        sort_lst = sort_lst + left_lst[i:]
 
    return sort_lst

def mergy_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = len(lst) // 2

    left_lst = mergy_sort(lst[:pivot])
    right_lst = mergy_sort(lst[pivot:])
    
    return mergy(left_lst, right_lst) 

lst = [100-i for i in range(100)]

mergy_sort(lst)
print(lst)