from leap_year import is_year_leap

def valid_data(year=0, month=0, day=0):
    if (type(year) is not int) or (type(month) is not int) or (type(day) is not int):
        return None
    if month < 1 or  month > 12:
        return None
    if day != 0:
        if day < 1 or day > days_of_month[month -1]:
            return None
    return "Valid"

def days_in_month(year, month):
    if valid_data(year, month) == None:
        return None

    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days_of_month[1] += 1
    return days_of_month[month - 1]


'''
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "-> ", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
'''
