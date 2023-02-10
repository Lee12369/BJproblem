import math
def mergy_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = math.ceil(len(lst) / 2)
    left = mergy_sort(lst[:pivot])
    right = mergy_sort(lst[pivot:])
    
    return  mergy(left, right, lst_save)

def mergy(left_lst, right_lst, lst_save):
    
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
    
    if j == len(right_lst):
        sort_lst = sort_lst + left_lst[i:]

    lst_save.extend(sort_lst)
   
    return sort_lst

lst_save = []
N, K = map(int, input().split())
lst = list(map(int,input().split()))

mergy_sort(lst)

if K <= len(lst_save):
    answer = lst_save[K - 1]
else:
    answer = -1

print(answer)