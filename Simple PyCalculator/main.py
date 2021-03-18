from art import logo


def clear():
    print("\n" * 100)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


def py_calculator():

    operators = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': division,
    }

    choice = 'y'

    print("Starting a fresh calculation....\n")
    num1 = float(input("Enter your first number: "))

    while choice == 'y':

        print("\nBelow are the list of operators:")
        for symbol in operators:
            print(f"->\t{symbol}")

        operator_symbol = input("Pick an operator symbol from above: ")


        num2 = float(input("\nEnter your next number: "))

        answer = operators[operator_symbol](num1, num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")


        choice = input("\n1. Want to continue calculation?(Y/N)\n2. Exit - E\nEnter choice: ").lower()

        if choice == 'n':
            clear()
            py_calculator()
        elif choice == 'e':
            print("\nTHANK YOU 😄 👋")
            exit()

        clear()
        print("\nContinuing calculation....")
        print(f"Last saved result = {answer}")
        num1 = answer




if __name__ == '__main__':
    print(logo)
    print("\nWELCOME TO THE PyCALCULATOR 😊 🙏\n")
    py_calculator()