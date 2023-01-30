sci_grades = [int(input()) for _ in range(4)]
hist_grades = [int(input()) for _ in range(2)]

sum_sci3 = sum(sci_grades) - min(sci_grades)
max_hist = max(hist_grades)

answer = sum_sci3 + max_hist

print(answer)

