# Use filter and lambda to filter out all strings that
# start with the letter 'a' from a list of strings,
# but only if the string is longer than 3 characters.

def main():
    words = ["apple", "banana", "orange", "avocado", "pear", "kiwi", "apricot", "ale", "grape", "peach", 'an', 'as', 'at', 'am', 'ax']
    word_a_longer_than_3 = list(filter(lambda x: (x[0] == 'a' and len(x) > 3), words))
    print(word_a_longer_than_3)


if __name__ == '__main__':
    main()
