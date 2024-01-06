import doctest


def get_digits(number):
    """Return a list of digits in an int or string."""
    string = str(number)
    return [x for x in string if x.isdigit()]


def get_digits_with_docstring(number):
    """Return a list of digits in an int or string.
    >>> get_digits("124c41")
    ['1', '2', '4', '4', '1']
    >>> get_digits(1213141)
    ['1', '2', '1', '3', '1', '4', '1']
    """
    string = str(number)
    return [x for x in string if x.isdigit()]


doctest.testmod()
