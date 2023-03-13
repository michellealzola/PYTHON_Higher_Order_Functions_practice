# Use regex to find all email addresses in a given string.

import re

def main():
    string = 'Please contact me at john@example.com for further information or support@example.org for technical assistance.'
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    emails = re.findall(pattern, string)
    print(emails)
    

if __name__ == '__main__':
    main()

