"""
Write a program that creates a datetime object for November 4, 2020 , 14:53:00. The object created should call the
strftime method with the appropriate format to display the following result:
"""

from datetime import datetime

dt = datetime.strptime('November 4,2020,14:53:00', '%B %d,%Y,%H:%M:%S')
print(dt)
print(datetime.strftime(dt, '%Y/%m/%d %H:%M:%S'))
print(datetime.strftime(dt, '%y/%B/%d %H:%M:%S %p'))  # %p for AM/PM
print(datetime.strftime(dt, '%a ,%Y %B %d'))  # %B for Full month name
print('Weekday: ', datetime.strftime(dt, '%w'))  # lower case w for week day
print('Day of Year: ', datetime.strftime(dt, '%j'))  # %j for day in year
print('Week number of the year: ', datetime.strftime(dt, '%W'))  # Upper case W for week number also can use %U