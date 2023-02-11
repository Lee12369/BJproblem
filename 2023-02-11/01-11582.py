import sys
input = sys.stdin.readline

def mergy_sort(lst):
    if len(lst) <= 1:
        return lst
    
    piv = len(lst) // 2
    left = mergy_sort(lst[:piv])
    right = mergy_sort(lst[piv:])    
    
    return mergy(left, right)

def mergy(left, right):
    lst_sort = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            lst_sort.append(right[j])
            j += 1

        elif left[i] < right[j]:
            lst_sort.append(left[i])
            i += 1
    
    if i == len(left):
        lst_sort += right[j:]
    
    if j == len(right):
        lst_sort += left[i:]

    return lst_sort

N = int(input())
nums = list(map(int, input().rstrip('\n').split()))
K = int(input())

M = N // K

for i in range(K):
    slice_nums = nums[i * M : (i + 1) * M]
    answer = mergy_sort(slice_nums)
    for x in answer:
        print(x, end=' ')

