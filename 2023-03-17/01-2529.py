import sys
input = sys.stdin.readline

K = int(input())
equal_lst = list(input().split())

nums = [i for i in range(10)]

lst = []
visited = [0 for _ in range(10)]
ans_lst = []
def back_tracking(idx, lst, visited):
    if len(lst) == K + 1:
        word = ''
        for x in lst:
            word += str(x)
        ans_lst.append(word)
        return 0
    
    for i in range(10):
        if visited[i] == 0:
            if ((equal_lst[idx] == '<') and (lst[-1] < nums[i])) or ((equal_lst[idx] == '>') and (lst[-1] > nums[i])):
                visited[i] = 1
                save_lst = lst + [nums[i]]
                save_idx = idx + 1

                back_tracking(save_idx, save_lst, visited)

                visited[i] = 0

for i in range(10):
    lst = [i]
    visited[i] = 1

    back_tracking(0, lst, visited)

    visited[i] = 0

print(ans_lst[-1])
print(ans_lst[0])