# Use list comprehension to create a new list of all prime numbers in a given range.
import math


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def main():
    lst = [9, 2, 5, 3, 7, 8, 6, 1]
    print(lst)

    prime_lst = [x for x in lst if isPrime(x)]
    print(prime_lst)


if __name__ == '__main__':
    main()

