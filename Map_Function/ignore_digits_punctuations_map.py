# Use map and lambda to convert a list of strings to uppercase,
# but ignore strings that contain digits or punctuation.

def hasNoDigitsPunctuation(phrase):
    return all(word.isalpha() or word.isspace() for word in phrase)


def main():
    str_list = ['Hello', 'world!', 'Python3', 'This is a sentence.']
    str_uppercase = map(lambda x: x.upper() if hasNoDigitsPunctuation(x) else x, str_list)
    print(f'{list(str_uppercase)}')


if __name__ == '__main__':
    main()


