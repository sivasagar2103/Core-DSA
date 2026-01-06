'''
Every 4 years is a leap year
Every 100 years is NOT a leap year
Every 400 years IS a leap year


year % 4 == 0: Ensures the year is divisible by 4.

year % 100 != 0: Excludes century years (100, 200, ..., 1900) 
unless they are divisible by 400.

year % 400 == 0: Allows century years that are divisible by 400.

'''

year = 2000

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")

else:
    print("not a leap year")

#using calendar module
import calendar

if calendar.isleap(year):
    print("leap")
else:
    print("not a leap year")

#using lambda function
is_leap = lambda year : year %400 == 0 or (year % 4 == 0 and year % 100 != 0)

if is_leap(year):
    print("leap")
else:
    print("not a leap year")