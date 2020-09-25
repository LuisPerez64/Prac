"""
Question: https://leetcode.com/problems/day-of-the-week/

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
"""


def day_of_the_week(day: int, month: int, year: int) -> str:
    from calendar import weekday
    d = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    x = weekday(year, month, day)
    l = d.get(x)
    return l


#         # Theres no real way to get this response without taking into account leap years.
#         # Which happen every 4 years. I'd have to ask for the first leap year and use
#         that as a basis for the calculation.
#         # 2020 is a leap year so pulling that into account, and
#         # Assuming year 4 was the first leap year

#         # Also the day of the week at the Jan 01, 1971
#         day_map = {
#             0: 'Friday',
#             1: 'Saturday',
#             2: 'Sunday',
#             3: 'Monday',
#             4: 'Tuesday',
#             5: 'Wednesday',
#             6: 'Thursday'
#         }
#         month_map = {31: [0, 2, 5,6,7,9,11],
#                     30: [3,4,8,10],
#                     28: [1], # 29 on leap years
#                 }
#         # Jan 1, 1971 was a friday
#         day_0 = 0
#         years = year - 1971
#         months = 12 - month # Month 0 -> Jan
#         days_passed = 0
#         for idx in range(1971, year):
#             if idx % 4 == 0:
#                 # is_leap_year so add another day
#                 days_passed += 1
#             days_passed += 365

#         for idx in range(1, months+1):
#             for days, mth in month_map.items():
#                 if mth == idx -1 :
#                     days_passed += days

#         if year % 4 == 0 and month > 1:
#             # Add another day as its a leap year and past february
#             days_passed += 1

#         days_passed += day + 1 # If the days index starts at 0 then 1 day needs to be added.
#         return day_map[days_passed % 7]

print(day_of_the_week(31, 8, 2019))
print(day_of_the_week(18, 7, 1999))
print(day_of_the_week(15, 8, 1993))
