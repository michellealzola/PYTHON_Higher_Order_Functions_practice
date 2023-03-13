# Use regex to extract all dates in the format "MM/DD/YYYY" from a given string.
import re


def main():
    string = "Today is 03/12/2023 and tomorrow is 03/13/2023."

    pattern = r'\d{2}/\d{2}/\d{4}'

    dates = re.findall(pattern, string)

    print(dates)


if __name__ == '__main__':
    main()

