import random
from tkinter import *

cards = [1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
dealer_cards = []
player_1_cards = []
player_2_cards = []

window_21 = Tk()
window_21.geometry("1920x1080")
window_21.title("21")

def dealer():
    while len(dealer_cards) < 2:
        dealer_cards.append(random.choice(cards))
    value = calculate(0, 0, dealer_cards)
    return value

def player_1():
    while len(player_1_cards) < 2:
        player_1_cards.append(random.choice(cards))
    value = calculate(0, 0, player_1_cards)
    return value

def player_2():
    while len(player_2_cards) < 2:
        player_2_cards.append(random.choice(cards))
    value = calculate(0, 0, player_2_cards)
    return value

def compete(value_dealer, value_player, player_cards):
    if value_dealer == 21:
        result.config(text="The dealer wins")
    elif value_dealer > value_player:
        result.config(text="The dealer wins")
    elif value_dealer < value_player:
        result.config(text="The player wins")
    elif value_dealer == value_player:
        value_dealer = adding(value_dealer, dealer_cards)
        value_player = adding(value_player, player_cards)
        return [value_dealer, value_player]

def calculate(current_value, index, card_set):
    while current_value <= 21 and index < len(card_set):
        if isinstance(card_set[index], int):
            current_value += card_set[index]
        elif card_set[index] in ["Queen", "King", "Jack"]:
            current_value += 10
        else:
            # Using a default value for Ace in GUI context
            current_value += 11
        index += 1
        result.config(text="Your current value is "+ str(current_value))
    return current_value

def adding(current_value, card_set):
    new_card = random.choice(cards)
    card_set.append(new_card)
    new_value = calculate(current_value, len(card_set) - 1, card_set)
    return new_value

def begin():
    dealer_cards.clear()
    player_1_cards.clear()
    player_2_cards.clear()

    d_value = dealer()
    p1_value = player_1()
    p2_value = player_2()
    in_play = player.get()











