# Write a function that takes a list of names and
# returns a list of their corresponding initials.

def initials(name_list):
    return list(map(lambda x: x[0], name_list))


def main():
    name_list = ['Alice Smith', 'Bob Johnson', 'Charlie Brown', 'David Lee']
    initials_list = initials(name_list)
    print(initials_list)


if __name__ == '__main__':
    main()
