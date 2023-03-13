# Use reduce and lambda to find the product of all numbers in a list,
# and handle the case where the list is empty by returning 1.

import functools

def main():
    list1 = [5, 8, 9, 4, 1, 1, 7, 2, 8]
    list2 = []

    product_list1 = functools.reduce(lambda x, y: x * y, list1, 1)
    product_list2 = functools.reduce(lambda x, y: x * y, list2, 1)

    print('The products for each list:')
    print(f'List1: {product_list1}')
    print(f'List2: {product_list2}')


if __name__ == "__main__":
    main()
