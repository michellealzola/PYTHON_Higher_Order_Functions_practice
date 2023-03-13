# Use reduce and lambda to find the maximum value in a list of integers.

import functools
import random


def main():
    numbers = []
    for i in range(1, 15):
        numbers.append(random.randint(1, 25))

    print(numbers)

    max_num = functools.reduce(lambda x, y: max(x, y), numbers)
    print(max_num)


if __name__ == '__main__':
    main()
