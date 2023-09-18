import sys
input = sys.stdin.readline

def get_change_points(nums):
    change_points = set()
    i = 0
    while i < N:
        # 초기 위치와 다른 경우
        if nums[i] != (i + 1):
            start = int(i)
            # 값의 차이가 1씩 차이가 나지 않을 때까지 이동
            while (i + 1) < N and abs(nums[i] - nums[i + 1]) == 1:
                i += 1
            end = int(i)
            change_points.add(start)
            change_points.add(end)
        i += 1
    return list(change_points)

def back_tracking(change_points, nums, commands, cnt):
    if nums == target:
        answer.extend(commands)
        # 0 or 1 번만으로도 원래 위치와 일치하는 경우를 대비
        for _ in range(2 - cnt):
            answer.append((0, 0))
        return
    
    # 첫 번째 뒤집기
    if cnt == 0:
        M = len(change_points)
        # check_points 안에 값들을 이용하여 뒤집기 실행
        for i in range(M):
            for j in range(M):
                x = change_points[i]
                y = change_points[j]
                if x > y:
                    continue
                temp = nums[: x] + nums[x : y + 1][::-1] + nums[y + 1 :]

                back_tracking(change_points, temp, [(x, y)], cnt + 1)

    # 두 번째 뒤집기, 여기서는 전부 찾는것이 아니라 마지막으로 뒤집어야 하기에 뒤집을 구간 하나만을 찾으면 된다. 
    if cnt == 1:
        i = 0
        while i < N:
            if nums[i] != (i + 1):
                start = int(i)
                while (i + 1) < N and abs(nums[i] - nums[i + 1]) == 1:
                    i += 1
                end = int(i)
                temp = nums[: start] + nums[start : end + 1][::-1] + nums[end + 1 :]
                return back_tracking(change_points, temp, commands + [(start, end)], cnt + 1)
            i += 1

N = int(input())
nums = list(map(int, input().split()))
target = [i for i in range(1, N + 1)]

answer = []
commands = []
cnt = 0
change_points = get_change_points(nums)

back_tracking(change_points, nums, commands, cnt)

# 출력
for i in range(2):
    x, y = answer[i]
    print(x + 1, y + 1)