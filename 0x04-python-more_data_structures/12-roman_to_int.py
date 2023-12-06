#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    roman_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    n = len(roman_string)
    ans = 0
    i = 0
    while i < n:
        if roman_dict.get(roman_string[i], 0) == 0:
            return 0
        if i == n - 1 and roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            ans = ans + roman_dict[roman_string[i]]
        else:
            ans = ans + roman_dict[roman_string[i]] * -1
            i += 1
    return ans
