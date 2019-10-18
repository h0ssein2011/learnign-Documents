import calendar

mm,dd,yy=map(int , input().split())
ind=calendar.weekday(yy,mm,dd)
print(list(calendar.day_name)[ind].upper())
