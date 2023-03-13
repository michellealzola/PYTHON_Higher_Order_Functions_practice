# Sort a list of dictionaries based on a specific key.

def main():
    people = [{'name': 'Alice', 'age': 25},
              {'name': 'Bob', 'age': 20},
              {'name': 'Charlie', 'age': 30},
              {'name': 'David', 'age': 22}]

    people_sorted = sorted(people, key=lambda x: x['age'])
    print(people_sorted)


if __name__ == '__main__':
    main()
