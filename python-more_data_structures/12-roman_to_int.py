#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    results = 0
    last_value = 0

    for char in reversed(roman_string):
        value = rom_num.get(char)
        if value < last_value:
            results -= value
        else:
            results += value
        last_value = value

    return results