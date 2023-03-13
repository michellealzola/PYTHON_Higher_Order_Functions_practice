# Sort a list of strings based on the length of the string.

def main():
    words = ['cat', 'dog', 'elephant', 'fish']
    words_sorted = sorted(words, key=lambda x: len(x))
    print(words_sorted)
    

if __name__ == '__main__':
    main()
