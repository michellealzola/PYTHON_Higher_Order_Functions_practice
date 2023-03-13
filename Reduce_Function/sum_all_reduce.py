# Use reduce and lambda to find the sum of all numbers in a list.

import functools

def main():
    numbers = [4.5, -7.2, -1.1, 0.5, -3.9, 2.0, 9.1, -6.7, 1.8, -5.5]
    sum_all = round(functools.reduce(lambda x, y: x + y, numbers), 2)
    print(sum_all)


if __name__ == '__main__':
    main()

