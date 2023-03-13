# Write a list comprehension that returns a list of all the possible
# Pythagorean triples (a, b, c) where a, b, and c are all integers
# between 1 and 100.

def main():
    pythagorean_triples = [(a, b, c)
                           for a in range(1, 101)
                           for b in range(1, 101)
                           for c in range(1, 101)
                           if (a ** 2 + b ** 2) == c ** 2]
    print(pythagorean_triples)


if __name__ == '__main__':
    main()

