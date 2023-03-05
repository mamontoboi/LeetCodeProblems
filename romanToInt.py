def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    number = 0
    i = 0

    if 'IV' in s:
        x = s.find('IV')
        number += 4
        s = s[:x] + s[x + 2:]

    if 'IX' in s:
        x = s.find('IX')
        number += 9
        s = s[:x] + s[x + 2:]

    if 'XL' in s:
        x = s.find('XL')
        number += 40
        s = s[:x] + s[x + 2:]

    if 'XC' in s:
        x = s.find('XC')
        number += 90
        s = s[:x] + s[x + 2:]

    if 'CD' in s:
        x = s.find('CD')
        number += 400
        s = s[:x] + s[x + 2:]

    if 'CM' in s:
        x = s.find('CM')
        number += 900
        s = s[:x] + s[x + 2:]

    for i in s:
        number += numbers[i]

    return number


print(romanToInt('MCMXCIV'))