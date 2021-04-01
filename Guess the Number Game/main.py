import random
from art import logo


def clear(): print("\n" * 100)


def check_guess(guess):

    if guess == random_number:
        print("WOOHOO!! You guessed it correct! 👏 🥳")
        return True

    elif guess > random_number:
        if abs(guess - random_number) > 10:
            print("\nToo high. Try lowering your number 👇")
        elif abs(guess - random_number) <= 2:
            print("\nYou are very close to the chosen number. Just a few more tries 🤞")
        elif abs(guess - random_number) <= 5:
            print("\nClose but not enough. Try lowering your number but slightly 😇")
        elif abs(guess - random_number) <= 10:
            print("\nStill high. Lower it a few more 🙌")


    else:
        if abs(guess - random_number) > 10:
            print("\nToo low. Try with a larger number 👆")
        elif abs(guess - random_number) <= 2:
            print("\nYou are very close to the chosen number. Just a few more tries 🤞")
        elif abs(guess - random_number) <= 5:
            print("\nClose but not enough. Try incrementing your number but slightly 😇")
        elif abs(guess - random_number) <= 10:
            print("\nStill low. Add a few extras to it 🙌")



    return False



def guessing_game():

    print(logo, end="\n\n")

    # print(f"Random number: {random_number}\n")

    difficulty = input("-Easy difficulty(E) 😎\n-Hard difficulty(H) 🤯\nEnter your difficulty: ").lower()

    if difficulty == 'e':
        lives = 10
    elif difficulty == 'h':
        lives = 5
    else:
        print("OOPS!🤭 Something went wrong\n")
        return

    while lives:
        chosen_number = int(input("\nEnter your guess: "))
        lives -= 1

        if check_guess(chosen_number):
            return
        else:
            print(f"\nGuesses left: {lives}")

    print("\nSorry you LOST! 😭\nYou used all your guesses")


if __name__ == '__main__':

    choice = 'y'
    while choice == 'y':
        random_number = random.randint(1, 100)
        guessing_game()
        choice = input("\n\nWant to play again?(Y/N): ").lower()

        clear()

    print("\nTHANK YOU! 🙏")