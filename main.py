from art import logo
from game import Game
from player import Player


print(logo)

while True:

    user_choice = input("Would you like to play? ")

    if "y" in user_choice:
        name1 = input("Enter name for X: ")
        name2 = input("Enter name for O: ")
        player1 = Player(name1)
        player2 = Player(name2, "O")
        game = Game(player1, player2)
    else:
        break
