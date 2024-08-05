import random
from tkinter import *

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Queen", "King", "Jack", "Ace"]
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
            decision = int(input("Do you wish for the Ace to be 11 or 1?"))
            current_value += decision
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

    if in_play == "dealer":
        d_value = calculate(d_value, len(dealer_cards), dealer_cards)
        while d_value <= 21:
            attempt = choice.get()
            if attempt == "yes" or d_value < 16:
                d_value = adding(d_value, dealer_cards)
            else:
                break
        if d_value > 21:
            result.config(text="All players win")
    elif in_play == "player 1":
        p1_value = calculate(p1_value, len(player_1_cards), player_1_cards)
        while p1_value <= 21:
            attempt = choice.get()
            if attempt == "yes":
                p1_value = adding(p1_value, player_1_cards)
            else:
                new = compete(d_value, p1_value, player_1_cards)
                if new:
                    p1_value = new[1]
                    d_value = new[0]
                break
        if p1_value > 21:
            result.config(text="Player 1 is bust")
    elif in_play == "player 2":
        p2_value = calculate(p2_value, len(player_2_cards), player_2_cards)
        while p2_value <= 21:
            attempt = choice.get()
            if attempt == "yes":
                p2_value = adding(p2_value, player_2_cards)
            else:
                new = compete(d_value, p2_value, player_2_cards)
                if new:
                    p2_value = new[1]
                    d_value = new[0]
                break
        if p2_value > 21:
            result.config(text="Player 2 is bust")

    cont = Button(window_21,
                  text="Do you wish to play again?",
                  font=("Arial", 20, "bold"),
                  fg="red", bg="black",
                  command=begin)
    cont.pack(pady=30)

in_player = Label(window_21,
                  text="Input player (dealer, player 1, player 2)",
                  font=("Arial", 15, "bold"),
                  fg="red", bg="black",)

player = Entry(window_21,
               font=("Arial", 20, "bold"),
               fg="red", bg="black",)

submit_player = Button(window_21,
                       text="Submit Player",
                       font=("Arial", 20, "bold"),
                       fg="red", bg="black",
                       command=begin)

info = Label(window_21,
             text="Do you wish draw more cards",
             font=("Arial", 15),
             fg="blue", bg="black")

choice = Entry(window_21,
               font=("Arial", 20, "bold"),
               fg="red", bg="black",)

submit_choice = Button(window_21,
                       text="Submit Choice",
                       font=("Arial", 20, "bold"),
                       fg="red", bg="black",
                       command=adding)

result = Label(window_21,
               text="",
               font=("Arial", 20, "bold"),
               fg="red", bg="black",)

in_player.pack()
player.pack(pady=30)
submit_player.pack(pady=30)
info.pack()
choice.pack(pady=30)
submit_choice.pack()
result.pack(pady=30)

window_21.mainloop()
