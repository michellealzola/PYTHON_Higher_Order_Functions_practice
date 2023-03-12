# Use map and lambda to convert a list of strings to uppercase,
# and remove any leading/trailing whitespace before converting to uppercase.

def main():
    strings = ['   hello', 'world  ', '  foo bar  ', '   baz   ']
    str_uppercase_list = map(lambda x: x.strip().upper(), strings)
    print(f'{list(str_uppercase_list)}')


if __name__ == '__main__':
    main()
