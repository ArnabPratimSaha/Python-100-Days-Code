import random
import hangman_art
import hangman_words



def hang_man():

    print(hangman_art.logo, end="\n\n")

    chosen_word = random.choice(hangman_words.word_list)

    lives = len(hangman_art.stages) - 1

    display = []
    for _ in range(len(chosen_word)):
        display += '_'


    while '_' in display:
        guess = input("Guess a letter?: ").lower()


        if guess in display:
            print(f"\nYou have already guessed this letter '{guess}'")

        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess


        if guess not in chosen_word:
            print(f"\nYou guessed '{guess}', a wrong letter.\nYou lost a life")
            lives -= 1

        print(f"\nLives left: {lives}\n")

        print(" ".join(display))

        if lives == 0:
            print(hangman_art.stages[lives])
            break

        print(hangman_art.stages[lives])

    if lives == 0:
        print("GAME OVER!\nYOU LOST!! ☹")
    else:
        print("HURRAY YOU WON! 😄 👏")

    print("\n\nTHANK YOU FOR TRYING THE PROGRAM 🙏 🙏")



if __name__ == '__main__':
    hang_man()