import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tree_heights = list(map(int, input().rstrip('\n').split()))

tree_max_height = max(tree_heights)
tree_min_height = 0

while True:
    pivot = (tree_max_height + tree_min_height) // 2
    get_tree = 0
    for x in tree_heights:
        if x > pivot:
            get_tree += x - pivot
        else:
            pass
    if get_tree == M or tree_min_height == pivot:
        break
    
    elif get_tree > M:
        tree_min_height = pivot

    elif get_tree < M:
        tree_max_height = pivot

print(pivot)
