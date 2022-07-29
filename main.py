year = 2022

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if year in [2024]:
    week_day = 0
elif year in [2022]:
    week_day = 5
else:
    week_day = 6

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
month_number = 1

for month in months:
    if month in ['january', 'march', 'may', 'july', 'august', 'october', 'december']:
        month_length = 31
    elif month in ['april', 'june', 'september', 'november']:
        month_length = 30
    else:
        if (year % 400 == 0) and (year % 100 == 0):
            month_length = 29
        elif (year % 4 ==0) and (year % 100 != 0):
            month_length = 29
        else:
            month_length = 28

    for day in range(month_length):
        day += 1

        if month_number < 10:
            if day < 10:
                print(f'0{month_number}/0{day}/{year} {days[week_day]}')
            else:
                print(f'0{month_number}/{day}/{year} {days[week_day]}')
        else:
            if day < 10:
                print(f'{month_number}/0{day}/{year} {days[week_day]}')
            else:
                print(f'{month_number}/{day}/{year} {days[week_day]}')
                    
        if week_day == 6:
            week_day = 0
        else:
            week_day += 1

    month_number += 1
