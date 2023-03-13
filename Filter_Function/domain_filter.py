# Given a list of email addresses, filter out all the
# addresses that belong to a specific domain.

def domain_filter(address_list, domain):
    return list(filter(lambda x: x.endswith('@' + domain), address_list))

def main():
    email_addresses = ['jane@example.com', 'john@example.net', 'mark@example.com', 'jane@example.net', 'alice@example.com']
    domain = 'example.net'
    email_filtered = domain_filter(email_addresses, domain)
    print(email_filtered)


if __name__ == '__main__':
    main()

