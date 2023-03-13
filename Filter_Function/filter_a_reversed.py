# Use filter and lambda to filter out all strings that
# start with the letter 'a' from a list of strings, and
# return the filtered list in reverse order.

def main():
    words = ["apple", "banana", "orange", "avocado", "pear", "kiwi", "apricot", "grape", "peach"]
    words_starting_a = sorted(list(filter(lambda x: x[0] == 'a', words)), reverse=True)
    print(words_starting_a)


if __name__ == '__main__':
    main()

