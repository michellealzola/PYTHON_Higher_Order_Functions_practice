# Use filter and lambda to filter out all negative numbers from
# a list of integers that are stored as strings.

def main():
    num_strings = ['1', '-23', '456', '7890', '-123456789']
    num_negative_filtered = list(filter(lambda x: int(x) < 0, num_strings))
    print(num_negative_filtered)


if __name__ == '__main__':
    main()


