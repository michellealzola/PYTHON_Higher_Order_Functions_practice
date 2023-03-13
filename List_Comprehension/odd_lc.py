# Use list comprehension to create a new list of all odd numbers in a given list.

def main():
    lst = [9, 2, 5, 3, 7, 8, 6, 1]
    print(lst)

    odd_lst = [x for x in lst if x %2 != 0]
    print(odd_lst)


if __name__ == '__main__':
    main()
