calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    s = str(string)
    result = (len(s), s.upper(), s.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('AnacondaZ'))
print(string_info('NoizeMC'))
print(string_info('Tones and I'))
print(string_info('25/17'))
print(is_contains('Animal ДжаZ', ['АнимациЯ', 'aNimAL дЖАz', 'Каста']))
print(is_contains('Fun Mode', ['Eminem', 'Би-2', 'Uma2rman']))
print(calls)