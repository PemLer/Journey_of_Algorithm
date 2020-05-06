class Solution:
    def dayOfYear(self, date: str) -> int:

        def is_leap(year):
            flag = False
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                flag = True
            return flag

        def parse(date):
            items = date.split('-')
            year, month, day = map(int, items)
            return year, month, day

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year, month, day = parse(date)
        flag_leap = is_leap(year)
        count = 0
        i = 1
        while i < month:
            if i == 2 and flag_leap:
                count += 29
            else:
                count += month_days[i-1]
            i += 1
        count += day
        return count
