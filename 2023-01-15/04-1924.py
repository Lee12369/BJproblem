x, y = map(int, input().split())
day = [31,28,31,30,31,30,31,31,30,31,30,31]
day_sum = y

for i in range(0, x-1):
    day_sum += day[i]

week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
print(week[day_sum % 7])
