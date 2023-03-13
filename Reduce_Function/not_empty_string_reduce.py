# Use reduce and lambda to concatenate all strings in a list,
# but only if the string is not empty.

from functools import reduce


def main():
    strings = ['hello', '', 'world', '', 'python']
    concatenate = reduce(lambda x, y: x + y if y else x, strings)
    print(concatenate)


if __name__ == '__main__':
    main()
