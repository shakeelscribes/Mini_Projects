from art import logo
print(logo)

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_card = []
comp_card = []

for i in range(0,2):
    user_card.append(random.choice(cards))
    comp_card.append(random.choice(cards))

print(f"Your Cards: {user_card}, Current Score: {sum(user_card)}")
print(f"Computer's First Card: {comp_card[0]}")

exceeds_21 = False

while not exceeds_21:

    another_card = input("Type 'y' to get another Card, Type 'n' to pass: ").lower()

    if another_card == "y":
        user_card.append(random.choice(cards))
        if sum(user_card) > 21:
            print(f"Your Final Hand is {user_card} , final Score: {sum(user_card)}")
            print("You Went Over, You Lose!😭")
            exceeds_21 = True
        else:
            print(f"Your Cards: {user_card}, Current Score: {sum(user_card)}")
            print(f"Computer's First Card: {comp_card[0]}")

    elif another_card == "n":
        com_choice = False
        while not com_choice:
            comp_card.append(random.choice(cards))
            if sum(comp_card) > 21:
                print(f"Computer's Final Hand is {comp_card}, Final Score: {sum(comp_card)}")
                print("You Win!")
                exceeds_21  = True
                com_choice = True
            else:
                print(f"Your Cards: {user_card}, Current Score: {sum(user_card)}")
                print(f"Computer's First Card: {comp_card[0]}")