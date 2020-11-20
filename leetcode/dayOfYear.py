class Solution:
    def dayOfYear(self, date: str):
        _DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def is_leapyear(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        def days_in_month(year, month):
            if month == 1 and is_leapyear(year):
                print(is_leapyear(year))
                return 29
            else:
                return _DAYS_IN_MONTH[month]
                
        d = date.split('-')
        year, month, day = int(d[0]), int(d[1]), int(d[2])
        print(year, month, day)

        return sum([days_in_month(year, m) for m in range(0, month - 1)]) + day

class Solution2:
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): days[1] = 29
        return d + sum(days[:m-1])

class Solution3:
    def dayOfYear(self, date: str) -> int:
        y, m, d = (int(x) for x in date.split("-"))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        return sum(days[:(m-1)]) + d + (m > 2 and (y%4 == 0 and y%100 != 0 or y%400 == 0))

answer = Solution()
print(answer.dayOfYear("2004-03-01"))

'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 
Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.

'''