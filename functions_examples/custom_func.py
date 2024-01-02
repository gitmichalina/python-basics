def main():
    pass


def largest(a, b, c):
    """Return the largest of a, b, and c."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


if __name__ == "__main__":
    main()

