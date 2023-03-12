# •	Use map and lambda to convert a list of integers to
# their corresponding binary representation, and
# return a string representation of the binary number
# with leading zeroes to fill up to 8 digits.

def main():
    integers = [10, 20, 30, 40, 50, 60]
    binary = map(lambda x: bin(x)[2:].zfill(8), integers)
    print(f'{list(binary)}')


if __name__ == '__main__':
    main()
