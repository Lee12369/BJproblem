numbers = list(map(int,input().split())) # 숫자 세 개를 띄어쓰기를 이용해 한 줄로 입력한다.
numbers.remove(max(numbers))
numbers.remove(min(numbers))
print(numbers[0])
