# Use map and lambda to convert a list of integers to their
# corresponding Roman numerals.

def roman_int(num):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    roman_numeral = ''
    for number, roman in roman_numerals.items():
        if num >= number:
            roman_numeral += roman
            num -= number

    return roman_numeral


def main():
    integers_list = [10, 20, 30, 40, 50, 60]
    roman_list = map(lambda x: roman_int(x), integers_list)
    print(f'{list(roman_list)}')


if __name__ == '__main__':
    main()
