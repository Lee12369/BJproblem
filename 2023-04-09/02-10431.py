P = int(input())
for _ in range(P):
    nums = list(map(int, input().split()))
    T = nums[0]
    heights = nums[1:]

    line = []
    total_cnt = 0
    for i in range(20):
        line.append(heights[i])
        curr = len(line) - 1
        cnt = 0
        while curr > 0:
            if line[curr] < line[curr - 1]:
                line[curr], line[curr - 1] = line[curr - 1], line[curr]
                curr -= 1
                cnt += 1
            else:
                break

        total_cnt += cnt   

    print(T, total_cnt)