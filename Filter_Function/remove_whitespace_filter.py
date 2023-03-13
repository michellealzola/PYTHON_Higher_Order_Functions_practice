# Use filter and lambda to filter out all whitespace characters from a string.

def main():
    string = "This is a string with spaces and\ttabs"
    no_space = filter(lambda char: not char.isspace(), string)
    no_space_string = ''
    for char in no_space:
        no_space_string += char

    print(no_space_string)


if __name__ == '__main__':
    main()





