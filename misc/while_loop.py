def main():

    n = 2
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")

    n = 2
    while (n := n - 1) > 0:
        print(n)
    print("Blast off!")


if __name__ == "__main__":
    main()