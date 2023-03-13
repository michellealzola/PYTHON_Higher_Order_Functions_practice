# Use reduce and lambda to concatenate all strings in a list.

import functools

def main():
    strings = ['Hello', 'world!', 'Python', 'is amazing!']
    concatenate = functools.reduce(lambda x, y: x + ' ' + y, strings)
    print(concatenate)


if __name__ == '__main__':
    main()


