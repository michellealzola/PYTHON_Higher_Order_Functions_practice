# Write a function that takes a list of strings and a
# function f as arguments, and returns a list of strings that
# meet a certain condition based on f.

def filtera(word_list, f):
    return list(filter(lambda x: f(x), word_list))


def main():
    words = ["apple", "banana", "orange", "avocado", "pear", "kiwi", "apricot", "grape", "peach"]
    words_starting_a = filtera(words, lambda x: x[0] == 'a')
    print(list(words_starting_a))

    letter_not_in_word = filtera(words, lambda x: 'n' not in x)
    print(letter_not_in_word)


if __name__ == '__main__':
    main()

