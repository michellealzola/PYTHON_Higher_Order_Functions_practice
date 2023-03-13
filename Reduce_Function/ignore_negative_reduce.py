# Use reduce and lambda to find the maximum value in a list of integers,
# but ignore any negative numbers in the list.

from functools import reduce


def main():
    numbers = [-4.5, 7.2, -1.1, 0.5, -3.9, 2.0, 9.1, -6.7, 1.8, -5.5]
    max_num = reduce(lambda x, y: max(x, y) if y > 0 else x, numbers)
    print(max_num)


if __name__ == '__main__':
    main()
