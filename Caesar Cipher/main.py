import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar_cipher():

    print(art.logo)
    print("\n\nWELCOME TO THE CAESAR CIPHER")

    choice = 'y'

    while choice == 'y':
        direction = input("\n\n*\t'E' for ENCODE\n*\t'D' for DECODE\nProvide your choice: ").lower()
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))

        if direction == 'e' or direction == 'd':
            ciphering(text, shift, direction)
        else:
            print("\nOOPS!🤕 Something went wrong, renter again")
            continue


        choice = input("\nDo you want to go again? (Y/N): ").lower()

    print("\nGoodbye 👋\nTHANK YOU! 😄 🙏")


def ciphering(start_text, shift, choice):
    final_text = ""

    if choice == 'd':
        shift *= -1

    for char in start_text:
        upper_flag = False
        if char.isalpha():

            if char.isupper():
                upper_flag = True
            index = (alphabet.index(char.lower()) + shift) % 26

            if upper_flag:
                final_text += alphabet[index].upper()
            else:
                final_text += alphabet[index]
        else:
            final_text += char

    if choice == 'e':
        print(f"\nThe ENCRYPTED text is: {final_text}")
    else:
        print(f"\nThe DECRYPTED text is: {final_text}")


if __name__ == '__main__':
    caesar_cipher()
