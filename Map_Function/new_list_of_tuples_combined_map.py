# Create a new list of tuples based on two separate lists.

def main():
    numbers = [1, 2, 3, 4]
    letters = ['a', 'b', 'c', 'd']
    new_tuple = map(lambda x, y: (x, y), numbers, letters)
    print(f'{list(new_tuple)}')


if __name__ == '__main__':
    main()
