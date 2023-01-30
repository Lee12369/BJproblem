def heap_sort(lst):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, i, n)

    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i)

    return lst

def heapify(lst, idx, heap_size):
    max_idx = idx
    left = 2 * idx
    right = 2 * idx + 1

    if left < heap_size and lst[right] > lst[max_idx]:
        max_idx = left
    
    if right < heap_size and lst[right] > lst[max_idx]:
        max_idx = right
    
    if max_idx != idx:
        lst[max_idx], lst[idx] = lst[idx], lst[max_idx]
        heapify(lst, max_idx, heap_size)

lst = [i for i in range(100,0,-1)]
heap_sort(lst)
print(lst)