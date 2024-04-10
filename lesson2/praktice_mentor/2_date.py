from datetime import datetime


class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = date_str.split('-')
        return cls(int(day), int(month), int(year))

    @staticmethod
    def is_date_valid(date_value):
        date = Date.from_string(date_value)
        if date.day in range(1,32) and date.month in range(1,13):
            return True
        return False
    

date = Date.from_string('23-09-2022')
print(date.day)
print(date.month)
print(date.year)
print(Date.is_date_valid('23-09-2022'))
print(Date.is_date_valid('23-15-2022'))
print(Date.is_date_valid('32-09-2022'))