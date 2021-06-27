"""
During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new
method called count_weekday_in_year, which takes a year and a weekday as parameters, and then returns the number of
occurrences of a specific weekday in the year.

Use the following tips:
Create a class called MyCalendar that extends the Calendar class; create the count_weekday_in_year method with the
year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday.
The method should return the number of days as an integer; in your implementation, use the monthdays2calendar method
of the Calendar class.
"""

import calendar


class MyCal(calendar.Calendar):

    def __init__(self):
        super().__init__()
        self.__count = 0

    def count_weekday_in_year(self, __year=2021, __day=6):
        for month in range(1, 13):
            for data in self.monthdays2calendar(__year, month):
                for tup in data:
                    if tup[0] != 0 and tup[1] == __day:
                        self.__count += 1
        return self.__count


mc = MyCal()
print(mc.count_weekday_in_year(int(input('Enter the year : ')), int(input('Enter weekday to count : '))))