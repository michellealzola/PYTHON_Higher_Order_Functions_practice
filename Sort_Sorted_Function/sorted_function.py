# Write a function that takes a list of dictionaries and a lambda
# function f as arguments, and returns a list of dictionaries sorted
# based on the lambda function.

def sort_opr(lst, f):
    return sorted(lst, key=lambda x: f(x))


def main():
    people = [{'name': 'Alice', 'age': 25},
              {'name': 'Bob', 'age': 20},
              {'name': 'Charlie', 'age': 30},
              {'name': 'David', 'age': 22}]
    name_sorted = sort_opr(people, lambda x: x['name'])
    print(name_sorted)
    age_sorted = sort_opr(people, lambda x: x['age'])
    print(age_sorted)


if __name__ == '__main__':
    main()
