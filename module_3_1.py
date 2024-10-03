calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [x.lower() for x in list_to_search]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
#Вывод на консоль:
#(8, 'CAPYBARA', 'capybara')
#(10, 'ARMAGEDDON', 'armageddon')
#True
#False
#4