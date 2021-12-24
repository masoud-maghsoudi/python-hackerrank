import calendar

month, day, year = list(map(int, input().split()))
print("{}".format(calendar.day_name[calendar.weekday(year,month,day)]).upper())