# Use reduce and lambda to find the sum of all numbers in a list,
# but ignore any strings in the list.
import numbers
from functools import reduce

def main():
    mixed_list = [10, 20, 'hello', 30, 'world', 40]
    sum_num = reduce(lambda x, y: x + y if isinstance(y, numbers.Number) else x, mixed_list, 0)
    print(sum_num)


if __name__ == '__main__':
    main()

