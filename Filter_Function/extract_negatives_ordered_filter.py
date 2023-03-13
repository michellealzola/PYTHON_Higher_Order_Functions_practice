# Use filter and lambda to filter out all negative numbers
# from a list of integers, and return the filtered list in descending order.

def main():
    numbers = [4.5, -7.2, -1.1, 0.5, -3.9, 2.0, 9.1, -6.7, 1.8, -5.5]
    negative_nums = filter(lambda x: x < 0, numbers)
    print(sorted(list(negative_nums), reverse=True))


if __name__ == '__main__':
    main()
