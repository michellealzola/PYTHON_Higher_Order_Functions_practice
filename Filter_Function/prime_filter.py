# Given a list of numbers, filter out all the numbers that are prime.
import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_prime = list(filter(lambda x: not is_prime(x), numbers))
    print(filter_prime)


if __name__ == '__main__':
    main()

