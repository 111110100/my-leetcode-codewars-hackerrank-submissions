from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return date(year, month, day).strftime("%A")

class Solution2:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 1971.1.1 is Friday

        runm = [0,31,29,31,30,31,30,31,31,30,31,30,31]
        notrunm = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        
        days = {0:'Thursday',1:'Friday',2:'Saturday',3:'Sunday',4:'Monday',5:'Tuesday',6:'Wednesday'}
        
        dlen = 0
        
        yeard = year-1971
        
        runy = sum([y%4 == 0 for y in range(1971,year)])
        notruny = yeard-runy
        
        dlen+= runy*366 + notruny*365
        
        if year%4 == 0:
            dlen += sum(runm[:month])
        else:
            dlen += sum(notrunm[:month])
        
        dlen += day
        return days[dlen%7]

answer = Solution2()
print(answer.dayOfTheWeek(26,4,1972))

'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"

Constraints:

The given dates are valid dates between the years 1971 and 2100.

def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        daysInWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] #1
        DaysByMonthMod7 = [0,3,2,5,0,3,5,1,4,6,2,4]; # 2
        if(month < 3) : year = year - 1 # 3
        return daysInWeek[(year + (year//4 - year//100 + year//400) + DaysByMonthMod7[month-1] + day) % 7]; # 4
'''
