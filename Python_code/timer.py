import self as self
class Timer:
    self.hh = 0
    self.mm = 0
    self.ss = 0

    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        return str(self.hh)+':'+str(self.mm)+':'+str(self.ss);

    def next_second(self):
        self.ss += 1
        if self.ss > 59:
            self.ss = 0
            self.mm += 1
            if self.mm > 59:
                self.mm = 0
                self.hh += 1
                if self.hh > 23:
                    self.hh = 0

    def prev_second(self):
        self.ss -= 1
        if self.ss < 0:
            self.ss = 59
            self.mm -= 1
            if self.mm < 0:
                self.mm = 59
                self.hh -= 1
                if self.hh < 0:
                    self.hh = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)