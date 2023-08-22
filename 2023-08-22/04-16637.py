from collections import deque
def sum(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c

def back_tracking(nums, signs, bracket):
    result = calculation(nums, signs, bracket)
    answer.append(result)

    for i in range(M):
        if bracket[i] == False:
            if i + 1 < M and bracket[i + 1] == True:
                continue
            if i - 1 >= 0 and bracket[i - 1] == True:
                continue
            bracket[i] = True

            back_tracking(nums, signs, bracket)

            bracket[i] = False

def calculation(nums, signs, bracket):
    new_nums = deque()
    num = nums[0]
    new_nums.append(num)

    new_signs = deque()
    # 괄호가 있는 거부터 계산
    for i in range(M):
        if bracket[i] == True:
            num1 = new_nums.pop()
            num2 = nums[i + 1]
            sign = signs[i]
            num = cal[sign](num1, num2)
            new_nums.append(num)

        elif bracket[i] == False:
            new_nums.append(nums[i + 1])
            new_signs.append(signs[i])

    # 나머지 차례대로 계산
    result = new_nums.popleft()
    for i in range(len(new_signs)):
        num = new_nums[i]
        sign = new_signs[i]
        result = cal[sign](result, num)
    
    return result

# N = 9
# equation = ['3','+','8','*','7','-','9','*','2']

cal = {
    '+' : sum,
    '-' : sub,
    '*' : mul
}

N = int(input())
equation = list(input())
nums = deque()
signs = deque()
for i in range(N):
    if i % 2 == 1:
        signs.append(equation[i])
    elif i % 2 == 0:
        nums.append(int(equation[i]))

M = len(signs)
bracket = [False for _ in range(M)]
answer = []

back_tracking(nums, signs, bracket)

ans = max(answer)

print(ans)
