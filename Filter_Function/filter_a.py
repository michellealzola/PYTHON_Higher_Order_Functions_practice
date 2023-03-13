# Use filter and lambda to filter out all strings that
# start with the letter 'a' from a list of strings.

def main():
    words = ["apple", "banana", "orange", "avocado", "pear", "kiwi", "apricot", "grape", "peach"]
    words_starting_a = filter(lambda x: x[0] == 'a', words)
    print(list(words_starting_a))


if __name__ == '__main__':
    main()

