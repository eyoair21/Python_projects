import random


# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def check_jack(user, comp):
    if 11 in user and sum(user) > 21:
        user.remove(11)
        user.append(1)
    elif 11 in comp and sum(comp) > 21:
        comp.remove(11)
        comp.append(1)
    else:
        return " "


def win_lose(user, comp):
    if sum(user) == 21 and sum(comp) == 21:
        return "!!!!!!!!!!!!!!!! BLACK JACK House WINS !!!!!!!!!!!!!!!!"
    elif sum(user) == 21:
        return "$$$$$$$$$$$$$$$$$$ Black Jack Player wins $$$$$$$$$$$$$$$$$$$$$$"
    elif sum(comp) == 21:
        return "!!!!!!!!!!!!!!!!!!!!! Black Jack House Wins !!!!!!!!!!!!!!!!!"
    elif sum(user) > sum(comp):
        return "$$$$$$$$$$$$$$ Player wins $$$$$$$$$$$$$$$$$$$$$$"
    elif sum(user) < sum(comp):
        return "!!!!!!!!!!!!!!!!!! House Wins !!!!!!!!!!!!!!!!!"
    elif sum(user) == sum(comp):
        return "<<<<<<<<<<<<<< GAME is a DRAW >>>>>>>>"


user_card = []
comp_card = []
for item in range(2):
    user_card.append(deal_cards())
    comp_card.append(deal_cards())


def black_jack():
    state_val = True
    while state_val:
        print(f"Player cards: {user_card}")
        print(f"Computer's first card: {comp_card[0]}")
        if sum(comp_card) < 17:
            comp_card.append(deal_cards())

        chec_val = input("Type 'Y' to get another card, type 'N' to pass: ").lower()

        if chec_val == 'n':
            print(f"Your final Hand: {user_card} = {sum(user_card)}")
            print(f"House final hand: {comp_card} = {sum(comp_card)}")
            print(check_jack(user_card, comp_card))
            print(win_lose(user_card, comp_card))
            state_val = False

        elif chec_val == 'y':
            user_card.append(deal_cards())



black_jack()
