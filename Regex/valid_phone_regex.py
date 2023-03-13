# Use regex to validate if a given string is a valid phone number.
import re


def main():
    pattern = r'\(\d{3}\) \d{3}-\d{4}'

    phone_numbers = ["(123) 456-7890", "(123) 45-67890"]

    filter_valid_phone = list(filter(lambda x: x if re.search(pattern, x) else '', phone_numbers))

    print(filter_valid_phone)





if __name__ == '__main__':
    main()
