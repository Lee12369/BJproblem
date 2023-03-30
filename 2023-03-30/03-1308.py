start_year, start_month, start_day = map(int, input().split())
end_year, end_month, end_day = map(int, input().split())

dic = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

def check_leap_year(year):
    if year % 400 == 0:
        leap_year = 1

    elif year % 100 == 0:
        leap_year = 0
    
    elif year % 4 == 0:
        leap_year = 1
    
    else:
        leap_year = 0
    
    if leap_year == 1:
        dic[2] = 29
    else:
        dic[2] = 28

    return leap_year
    
if end_year - start_year > 1000 or (end_year - start_year == 1000 and end_month >= start_month and end_day >= start_day):
    print('gg')

else:
    d_day = 0
    if end_year > start_year:
        check_leap_year(start_year)    
        for i in range(start_month + 1, 13):
            d_day += dic[i]
        d_day += dic[start_month] - start_day

        for i in range(start_year + 1, end_year):
            leap_year = check_leap_year(i) 
            if leap_year == 1:
                d_day += 366
            else:
                d_day += 365
        
        check_leap_year(end_year)    
        for i in range(1, end_month):
            d_day += dic[i]
        d_day += end_day

    elif end_year == start_year:
        check_leap_year(start_year)
        for i in range(start_month + 1, end_month):
            d_day += dic[i]

        if start_month == end_month:
            d_day += end_day - start_day

        else:
            d_day += dic[start_month] - start_day + end_day

    print("D-{}".format(d_day))
