number = None
while number is None:
    try:
        n = input("Enter an integer: ")
        number = int(n)
    except Exception:
        print("Try again!")
    print("Your number is", number)

    # try:
    # # code that could go wrong
    # except SomeErrorType:
    # # what to do if it goes wrong
    # finally:
    # # what to do afterwards