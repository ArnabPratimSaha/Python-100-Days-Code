from art import logo
import random


def clear():
    print("\n" * 100)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(card_hand):
    card_hand.append(random.choice(cards))


def check_ace(card_hand):
    if 11 in card_hand and sum(card_hand) > 21:
        card_hand[card_hand.index(11)] = 1


def blackjack():
    user_hand = []
    dealer_hand = []

    for _ in range(2):
        deal_card(user_hand)
        deal_card(dealer_hand)

    print(f"Your cards: {user_hand} and current score: {sum(user_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}\n")

    if sum(user_hand) == 21:
        print(f"Your final hand: {user_hand} and final score: {sum(user_hand)}")
        print(f"Dealer's final hand: {dealer_hand} and final score: {sum(dealer_hand)}\n")
        print("You scored a BLACKJACK!\nYou WIN!! 🥳")
        return


    if sum(dealer_hand) == 21:
        print(f"Your final hand: {user_hand} and final score: {sum(user_hand)}")
        print(f"Dealer's final hand: {dealer_hand} and final score: {sum(dealer_hand)}\n")
        print("Dealer scored a BLACKJACK\nYou LOST! 😱")
        return




    choice = input("-Type 'G' for another card\n-Type 'P' to pass\nEnter choice: ").lower()

    while choice == 'g':
        deal_card(user_hand)
        check_ace(user_hand)

        if sum(user_hand) <= 21:
            print(f"\nYour cards: {user_hand} and current score: {sum(user_hand)}\n")
        else:
            print(f"\nYour final hand: {user_hand} and final score: {sum(user_hand)}")
            print(f"Dealer's final hand: {dealer_hand} and final score: {sum(dealer_hand)}\n")
            print("You went over\nYou LOST! 😭")

            return

        choice = input("-Type 'G' for another card\n-Type 'P' to pass\nEnter choice: ").lower()



    while sum(dealer_hand) < 17:
        deal_card(dealer_hand)
        check_ace(dealer_hand)

    print(f"\nYour final hand: {user_hand} and final score: {sum(user_hand)}")
    print(f"Dealer's final hand: {dealer_hand} and final score: {sum(dealer_hand)}\n")


    if sum(user_hand) > sum(dealer_hand):
        print("You WIN!! 😄")
    elif sum(dealer_hand) > sum(user_hand):
        if sum(dealer_hand) > 21:
            print("Dealer went over! You WIN!! 😁")
        else:
            print("You LOST! 😖")
    else:
        print("Its a DRAW! 🙃")



if __name__ == '__main__':
    ch = 'y'

    while ch == 'y':
        print(logo, end="\n\n")
        blackjack()

        ch = input("\nDo you want to play again?(Y/N): ").lower()
        clear()

    print("THANK YOU! 🙏")