# Given a list of strings, filter out all the strings that are palindromes.

def main():
    strings = ['hello', 'racecar', 'world', 'level', 'python']
    palindrome_filter = list(filter(lambda x: x == x[::-1], strings))
    print(palindrome_filter)


if __name__ == '__main__':
    main()

