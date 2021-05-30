from self import self


class WeekDayError(Exception):
    pass


class Weeker:
    self.day = None

    def __init__(self, day):
        self.lst = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        if day in self.lst:
            self.day = day
        else:
            raise WeekDayError

    def __str__(self):
        return self.day

    def add_days(self, n):
        n = n + self.lst.index(self.day)
        n %= 7
        self.day = self.lst[n]

    def subtract_days(self, n):
        n %= 7
        n = abs(n - self.lst.index(self.day))
        self.day = self.lst[n]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
