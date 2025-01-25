def is_year_leap(year):
    # Leap year calculator
    # If the year is not divisible by 4, it is a common year.
    # If it is divisible by 4 but not by 100, it is a leap year.
    # If it is divisible by 100 but not by 400, it is a common year.
    # If it is divisible by 400, it is a leap year.
    #
    flag = None
    
    # Check if the year is within the Gregorian calendar period
    if year < 1582:
        print("Not within the Gregorian calendar period.")
    else:
    # Determine if it's a leap year or a common year
        if year % 4 != 0:
            flag = False
        elif year % 100 != 0:
            flag = True
        elif year % 400 != 0:
            flag = False
        else:
            flag = True

    return flag

def days_in_month(year, month):
    """This takes two arguments (a year and a month)and returns the number of days 
    for the given month/year pair."""
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_year_leap(year) and month == 2:
        return m[month - 1] + 1
    else:
        return m[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
