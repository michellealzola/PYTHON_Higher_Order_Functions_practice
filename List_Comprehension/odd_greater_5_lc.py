# Use list comprehension and lambda to create a new list of all
# odd numbers in a given list, but only if the number is greater than 5.

def main():
    lst = [9, 2, -5, 3, -7, 8, 6, 1, 9, -2, 5, 3, 7, 8, -6, 1]
    print(lst)

    list_odd_grtr_5 = [x for x in lst if x > 5 and x % 2 != 0]
    print(list_odd_grtr_5)


if __name__ == '__main__':
    main()
