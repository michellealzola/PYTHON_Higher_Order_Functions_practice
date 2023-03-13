# Use list comprehension to create a new list of all odd numbers
# in a given list of floats, and return the result in ascending order.

def main():
    numbers = [-4.5, 7.2, -1.1, 0.5, -3.9, 2.0, 9.1, -6.7, 1.8, -5.5]
    odd_lst = sorted([x for x in numbers if x % 2 != 0])
    print(odd_lst)


if __name__ == '__main__':
    main()


