calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    st = str(string)
    rt = (len(st), st.upper(), st.lower())
    count_calls()
    return rt

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
        else:
            result = False
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)