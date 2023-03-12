# Use map and lambda to convert a list of integers to their
# corresponding binary representation.

def main():
    numbers = [5, 10, 15, 20]
    binary = map(lambda x: bin(x), numbers)
    print(list(binary))


if __name__ == '__main__':
    main()
