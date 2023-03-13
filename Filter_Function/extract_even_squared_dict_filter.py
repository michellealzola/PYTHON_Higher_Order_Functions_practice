# Use filter and lambda to filter out all even numbers from a list.
import random


def main():
    number_list = [4, 10, 15, 14, 2, 9, 11, 9, 3, 6]
    even_num = list(filter(lambda x: x % 2 != 0, number_list))
    print(even_num)
    # squared_dict = {}
    # for num in even_num:
    #     squared_dict[num] = num ** 2

    squared_dict = {num: num ** 2 for num in even_num}

    print(squared_dict)


if __name__ == '__main__':
    main()
