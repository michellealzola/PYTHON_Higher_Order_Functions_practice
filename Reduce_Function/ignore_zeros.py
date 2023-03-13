# Use reduce and lambda to find the product
# of all numbers in a list, but ignore any zeros in the list.

import functools

def main():
    list1 = [5, 0, 8, 9, 4, 0, 1, 1, 0, 7, 2, 0, 8]
    product_list = functools.reduce(lambda x, y: x * y if y != 0 else x, list1)
    print(product_list)


if __name__ == '__main__':
    main()

