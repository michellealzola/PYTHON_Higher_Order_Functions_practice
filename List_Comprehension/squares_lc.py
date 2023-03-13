# Use list comprehension to create a new list of squares of
# all even numbers in a given list.

def main():
    lst = [9, 2, 5, 3, 7, 8, 6, 1]
    print(lst)

    x = lambda a: a ** 2
    squared_lst_even = [x(a) for a in lst if a % 2 == 0]
    print(squared_lst_even)


if __name__ == '__main__':
    main()
