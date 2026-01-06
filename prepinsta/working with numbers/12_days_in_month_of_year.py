def is_leap(year):
    res = False
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return res

def days_in_month(month, year):
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    
    if month == 2 and is_leap(year):
        return days[month - 1] + 1
    return days[month - 1]

month = 2
year = 2024
res = days_in_month(month, year)
print(res)
