# Write a list comprehension that returns a list of all the possible
# combinations of three letters from the word "python".
from itertools import combinations


def main():
    combi = [''.join(x) for x in combinations('python', 3)]
    print(combi)


if __name__ == '__main__':
    main()

