# Use list comprehension and lambda to create a new list
# of squares of all even numbers in a given list, but ignore any
# negative numbers in the list.

def main():
    lst = [9, 2, -5, 3, -7, 8, 6, 1, 9, -2, 5, 3, 7, 8, -6, 1]
    print(lst)

    x = lambda a: a ** 2
    squared_list_positive = [x(a) for a in lst if a % 2 == 0 and a > 0]
    print(squared_list_positive)


if __name__ == '__main__':
    main()

