def get_dig(number):
    """Return a list of digits in an int or string."""
    string = str(number)
    return [x for x in string if x.isdigit()]


def main():
    s = input("Enter something: ")
    digits = get_dig(s)
    print("Digits found:", digits)
    if digits != []:
        main()


# Call main() if and only if started from this file
if __name__ == '__main__':
    main()
