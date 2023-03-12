# Write a function that takes two lists of the same length
# and a function f as arguments, and returns a list where f
# has been applied to the corresponding elements of the two input lists.

def opr(list1, list2, f):
    return list(map(lambda x, y: f(x, y), list1, list2))


def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50]
    sum_list = opr(list1, list2, lambda x, y: x + y)
    print(sum_list)
    product_list = opr(list1, list2, lambda x, y: x * y)
    print(product_list)


if __name__ == '__main__':
    main()
