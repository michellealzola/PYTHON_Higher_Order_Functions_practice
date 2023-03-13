# Write a list comprehension that returns all the even numbers
# between 1 and 100 that are also divisible by 3.

def main():
    even_bet_1_100_div_3 = [x for x in range(1, 101) if x % 2 == 0 and x % 3 == 0]
    print(even_bet_1_100_div_3)


if __name__ == '__main__':
    main()

