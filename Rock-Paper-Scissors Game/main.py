import random

hand_symbols = ["""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """, """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """, """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """]


def rps_check(user_hand_symbol_index, comp_hand_symbol_index):
    if user_hand_symbol_index == 0:
        if comp_hand_symbol_index == 0:
            print("GAME IS TIE!")
        elif comp_hand_symbol_index == 1:
            print("YOU LOST!")
        else:
            print("YOU WON! CONGRATULATIONS 🙌")

    elif user_hand_symbol_index == 1:
        if comp_hand_symbol_index == 0:
            print("YOU WON! CONGRATULATIONS 🙌")
        elif comp_hand_symbol_index == 1:
            print("GAME IS TIE!")
        else:
            print("YOU LOST!")

    else:
        if comp_hand_symbol_index == 0:
            print("YOU LOST!")
        elif comp_hand_symbol_index == 1:
            print("YOU WON! CONGRATULATIONS 🙌")
        else:
            print("GAME IS TIE!")



def rps_game():
    play_game = 'y'

    print("WELCOME TO THE GAME OF ROCK, PAPER, SCISSORS")

    while play_game == 'y':
        user_hand = input("R - Rock\nP - Paper\nS - Scissors\nPut forward your symbol: ").lower()

        if user_hand == "r":
            user_hand_symbol_index = 0
        elif user_hand == "p":
            user_hand_symbol_index = 1
        elif user_hand == "s":
            user_hand_symbol_index = 2
        else:
            print("Provide a valid input!")
            continue

        comp_hand_symbol_index = random.randint(0, len(hand_symbols)-1)

        print("\n\n")
        print("Your Hand:")
        print(hand_symbols[user_hand_symbol_index])
        print("Computer Hand:")
        print(hand_symbols[comp_hand_symbol_index])



        rps_check(user_hand_symbol_index, comp_hand_symbol_index)

        play_game = input("\nDo you wanna have another try?(Y/N): ").lower()



    print("THANK YOU FOR PLAYING! 😄 🙏")


if __name__ == '__main__':
    rps_game()