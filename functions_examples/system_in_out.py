def main():
    name = input("What is your name? ")
    print("Hello,", name)

    question = "How old are you, " + name + "? "
    age = int(input(question))


if __name__ == "__main__":
    main()