def pass_check(string):
    pass_length(string)
    special_character(string)
    first_letter_check(string)
    print("Password check done!")


def pass_length(string):
    lungime = int(len(string))
    if lungime < 7:
        print("!!! Password length to short...exiting!")
        exit(1)
    print("Password length acceptable..")


def special_character(string):
    if not any(char in ['!', '@', '%'] for char in string):
        print("!!! Password needs at least 1 special character...exiting!")
        exit(1)
    print("Special character check passed..")


def first_letter_check(string):
    if string[0].isupper():
        print("Upper case first letter check..")
    else:
        print("!!! Passwords first letter is not upper case...exiting!")
        exit(1)


# username = input("Enter username: ")
password = input("Enter password: ")

pass_check(password)



