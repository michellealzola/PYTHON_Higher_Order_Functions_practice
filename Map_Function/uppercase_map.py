# Use map and lambda to convert a list of strings to uppercase

def main():
    str_list = ['hello', 'world', 'python', 'programming', 'is', 'fun']
    str_uppercase = map(lambda a: a.upper(), str_list)
    print(list(str_uppercase))


if __name__ == '__main__':
    main()
