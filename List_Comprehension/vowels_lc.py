# Write a list comprehension that returns a list of all
# the words in a sentence that are at least 3 characters
# long and start with a vowel.

def main():
    sentence = "The quick brown fox jumps over the lazy dog"
    vowels = [word for word in sentence.split() if len(word) >= 3 and
              word[0].lower() in ['a', 'e', 'i', 'o', 'u']]
    print(vowels)



if __name__ == '__main__':
    main()
