# Use list comprehension to create a new list of squares of
# all even numbers in a given list, and handle the case where
# the list is empty by returning an empty list.

def isEmpty(lst):
    if len(lst) == 0:
        return []
    else:
        return lst


def main():
    lst = [9, 2, 5, 3, 7, 8, 6, 1]
    print(lst)

    new_lst = [x ** 2 for x in lst if isEmpty(lst) and x % 2 == 0]
    print(new_lst)

    lst2 = []
    new_lst2 = [x ** 2 for x in lst2 if isEmpty(lst2) and x % 2 == 0]
    print(new_lst2)


if __name__ == '__main__':
    main()


