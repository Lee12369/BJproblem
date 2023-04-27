T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    
    HP = nums[0] + nums[4]
    if HP < 1:
        HP = 1
    
    MP = nums[1] + nums[5]
    if MP < 1:
        MP = 1

    Attack = nums[2] + nums[6]
    if Attack < 0:
        Attack = 0

    Defense = nums[3] + nums[7]

    Power = HP + 5 * MP + 2 * Attack + 2 * Defense

    print(Power)