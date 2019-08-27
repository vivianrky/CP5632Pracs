"""
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 7

def password_checker():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))

    print('*' * len(password))

def main():

    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    password = input("Enter password of at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


main()