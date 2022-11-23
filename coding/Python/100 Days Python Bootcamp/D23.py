import math

age = int(input("What is your current age?"))

def convert_days_left(age, death_year = 90):
    if age > 90:
        print('Please enter a valid age')
    else :
        years_remain = death_year - age
        days_remain = years_remain * 365
        weeks_remain = int(days_remain / 7)
        month_remain = int(days_remain / 30)
        return (f'You have {days_remain} days , {weeks_remain} weeks, and {month_remain} month left ')

print(convert_days_left(age))

