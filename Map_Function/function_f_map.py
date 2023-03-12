# Write a function that takes a list of numbers and a function f
# as arguments, and returns a list of numbers where f has been
# applied to each element.

def opr(num_list, f):
    return list(map(lambda x: f(x), num_list))


def main():
    num_list = [1, 2, 3, 4, 5]
    squared = opr(num_list, lambda x: x ** 2)
    print(squared)
    doubled = opr(num_list, lambda x: x * 2)
    print(doubled)


if __name__ == '__main__':
    main()
