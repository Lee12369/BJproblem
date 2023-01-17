import sys
std_attend_number = set([int(sys.stdin.readline()) for i in range(28)])
std_all_number = set([i for i in range(1,31)])
std_absent_number = std_all_number.difference(std_attend_number)

low_number = min(std_absent_number)
high_number = max(std_absent_number)

print(low_number)
print(high_number) 