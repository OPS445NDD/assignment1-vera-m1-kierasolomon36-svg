#!/usr/bin/env python3
"""
OPS445 Assignment 1 - Milestone 1
Author: Kiera Solomon/ksolomon6
"""
import sys

def leap_year(year: int) -> bool:
    """Return True if the year is a leap year, False otherwise."""
    lyear = year % 4
    if lyear == 0:
        feb_max = 29
    else:
        feb_max = 28

    lyear = year % 100
    if lyear == 0:
        feb_max = 28

    lyear = year % 400
    if lyear == 0:
        feb_max = 29
        
    return feb_max == 29

def mon_max(month: int, year: int) -> int:
    """Return the maximum number of days in a given month and year."""
    if leap_year(year):
        feb_max = 29
    else:
        feb_max = 28
        
    mon_dict = {1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return mon_dict[month]

def after(date: str) -> str:
    """Return the date for the next day of the given date."""
    # Splits the incoming 'YYYY-MM-DD' string into three separate string variables
    str_year, str_month, str_day = date.split('-')
    
    # Converts the string values into integers for math operations
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    # Use the refactored mon_max function passing both month and year
    max_days = mon_max(month, year)

    # Increments the current day by 1 to get the next calendar day
    tmp_day = day + 1  

    # Checks if the incremented day exceeds the maximum allowed days for the current month
    if tmp_day > max_days:
        to_day = tmp_day % max_days  # Roll the day back to 1 if it exceeds month max
        tmp_month = month + 1        # Move to next month
    else:
        to_day = tmp_day             # Keep the incremented day
        tmp_month = month + 0        # Month remains unchanged

    # Checks if the incremented month exceeds December (month 12)
    if tmp_month > 12:
        to_month = 1                 # Roll back to January
        year = year + 1              # Increment the year
    else:
        to_month = tmp_month + 0     # Keep the updated month

    # Formats the final date into a standard YYYY-MM-DD string with leading zeros
    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date

if __name__ == "__main__":
    pass
