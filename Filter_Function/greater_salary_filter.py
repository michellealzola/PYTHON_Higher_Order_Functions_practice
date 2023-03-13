# Given a list of dictionaries representing employees,
# filter out all the employees who have a salary greater than a certain amount.

def main():
    employees = [
        {'name': 'John', 'salary': 50000},
        {'name': 'Jane', 'salary': 70000},
        {'name': 'Mark', 'salary': 60000},
        {'name': 'Alice', 'salary': 80000},
        {'name': 'Bob', 'salary': 45000}
    ]
    min_salary = 60000
    salary_filtered = list(filter(lambda x: x['salary'] >= min_salary, employees))
    print(salary_filtered)



if __name__ == '__main__':
    main()
