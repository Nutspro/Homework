calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    count_calls()
    my_tuple = (len(string), string.upper(), string.lower())
    return my_tuple
def is_contains(string, list_to_search):
    count_calls()
    i = 0
    while i < len(list_to_search):
        list_to_search[i] = list_to_search[i].lower()
        i = i + 1
    return string.lower() in list_to_search
print(string_info('Banana'))
print(string_info('Pineapple'))
print(string_info('cat'))
print(is_contains('Paper', ['paPER', 'piper', 'apple'])) # Paper ~ paPER
print(is_contains('computer', ['competitor', 'company'])) # No matches
print(calls)