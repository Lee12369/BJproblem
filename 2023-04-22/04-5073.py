while True:
    line1, line2, line3 = map(int, input().split())
    if not (line1 and line2 and line3):
        break

    lines = [line1, line2, line3]
    total_length = sum(lines)
    max_length = max(lines)
    if total_length <= max_length * 2:
        print("Invalid")

    elif line1 != line2 != line3 != line1:
        print("Scalene")
    
    elif line1 == line2 == line3:
        print("Equilateral")
    
    else:
        print("Isosceles")


    