# Use filter and lambda to filter out all even numbers from a list.
import random


def main():
    number_list = []
    for i in range(10):
        num = random.randint(1, 15)
        number_list.append(num)
    print(number_list)

    even_num = filter(lambda x: x % 2 == 0, number_list)
    print(list(even_num))


if __name__ == '__main__':
    main()
