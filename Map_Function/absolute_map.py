# Write a function that takes a list of numbers and returns a
# list of their corresponding absolute values.

def absolute(num_list):
    return list(map(lambda x: abs(x), num_list))

def main():
    num_list = [-3, -2, -1, 0, 1, 2, 3]
    abs_list = absolute(num_list)
    print(abs_list)


if __name__ == '__main__':
    main()
