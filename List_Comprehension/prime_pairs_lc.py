# Write a list comprehension that returns all the pairs of integers (a, b)
# such that a and b are both prime numbers and a + b = 100.
import math


def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def main():
    nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print(nums)

    prime_pairs = [(a, b) for a in nums for b in nums if isPrime(a) and isPrime(b) and (a + b) == 100]
    print(prime_pairs)


if __name__ == '__main__':
    main()
