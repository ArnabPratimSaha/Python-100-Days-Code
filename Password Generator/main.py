import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():

    print("WELCOME TO THE PyPASSWORD GENERATOR!")

    number_letters = int(input("\nHow many letters would you want in your password?: "))
    number_symbols = int(input("How many symbols would you like?: "))
    number_numbers = int(input("How many numbers would you like?: "))

    password_list = []

    for _ in range(0, number_letters):
        password_list.append(random.choice(letters))

    for _ in range(0, number_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(0, number_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = " "
    for c in password_list:
        password += c

    print(f"\nYour UNCRACKABLE password is: {password}")
    print("\nTHANK YOU FOR! 😄")


if __name__ == '__main__':
    password_generator()