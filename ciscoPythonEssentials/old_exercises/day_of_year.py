from days_of_month import days_in_month, valid_data


def day_of_year(year, month, day):
    if valid_data(year, month, day) == None:
        day_of_year = None
        return day_of_year

    day_of_year = 0
    month_count = 1

    while month_count < month:
        day_of_year += days_in_month(year, month_count)
        month_count += 1
    day_of_year += day

    return day_of_year

### Tests ###
#print(day_of_year(2021, 11, 99)) #None

def test_days_of_year():
    # Datas for test
    years_to_test = [2000, 2021, 2005, 1988, 2006, 2009, "21", 2021, 2021]
    month_to_test = [12, 11, 3, 5, 10, 2, 23, 50, 11]
    days_for_test = [31, 10, 1, 29, 31, 29, 10, 10, 99]
    expected_results = [366, 314, 60, 150, 304, None, None, None, None]
    test_base = [years_to_test, month_to_test, days_for_test, expected_results]

    for test in range(len(test_base[0])):
        teste = []
        for data in range(len(test_base)):
            teste.append(test_base[data][test])
        print(f"Teste {test + 1} ", end="==> ")
        if day_of_year(teste[0], teste[1], teste[2]) == teste[-1]:
            print("Pass")
        else:
            print("Fail")

test_days_of_year()
