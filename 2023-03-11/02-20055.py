import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
robot = [False for _ in range(N * 2)]


up_robot = 0
down_robot = N - 1
stage = 1
while True:
    # 1
    up_robot -= 1
    down_robot -= 1
    if up_robot < -2 * N:
        up_robot += 2 * N
        down_robot += 2 * N 
    
    # 2
    for i in range(down_robot, up_robot - 1, -1):
        if robot[i] == True:
            next = i + 1
            if next < down_robot + 1 and nums[next] > 0 and robot[next] == False:
                nums[next] -= 1
                next += 1

            robot[i] = False
            robot[next - 1] = True
            if robot[down_robot] == True:
                robot[down_robot] = False

    # 3
    if nums[up_robot] > 0:
        robot[up_robot] = True
        nums[up_robot] -= 1

    # 4
    if nums.count(0) >= K:
        break

    stage += 1

print(stage)