def main():
    n = input("Print all primes up to: ")
    print_primes(int(n))


def is_prime(n):
    """Test if a number n is prime."""
    divisor = 2

    if n == 1:
        return False
    else:
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True


def print_primes(limit):
    for i in range(2, limit + 1):
        if is_prime(i):
            print(i, end=' ')


if __name__ == "__main__":
    main()
