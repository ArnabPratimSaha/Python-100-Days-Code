from art import logo


def clear():
    """
    Clears the output by adding 100 liens of end-line character
    """
    print("\n"*100)



auction = {}


def secret_auction():
    print(logo)
    print("\n\nWelcome to the SECRET AUCTION PROGRAM 🙏\n")

    choice = 'y'

    while choice == 'y':
        name = input("Mention your name?: ")
        bid = int(input("What's your bid?: ₹"))

        auction[name] = bid

        choice = input("\nAre there anymore bidders?(Y/N): ").lower()

        clear()

        if choice == 'n':
            break


    max_bid = 0
    person = ""
    for name in auction:
        if auction[name] > max_bid:
            max_bid = auction[name]
            person = name

    print(f"The winner is {person} with a bid amount of ₹{max_bid}.")
    print("\nTHANK YOU FOR USING THE PROGRAM 👋 😄")


if __name__ == "__main__":
    secret_auction()