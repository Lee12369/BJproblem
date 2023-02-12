N , X = map(int, input().split())

M = 1
patty = 1
for _ in range(N): 
    M = M * 2 + 3
    patty = patty * 2 + 1

left = 1
right = M
eat_patty = 0
while True:
    mid = (left + right) // 2
    patty = (patty - 1) // 2
    
    if X == left:
        break
    elif X == mid:
        eat_patty += patty + 1
        break
    elif X == right:
        eat_patty += patty * 2 + 1
        break
    
    if X > mid:
        left = mid + 1
        right -= 1
        eat_patty += patty + 1

    elif X < mid:
        left += 1
        right = mid - 1

    if left == right:
        eat_patty += 1
        break

print(eat_patty)