"""
projekt_2_2.py: druhý projekt do Engeto Online Python Akademie

author: Pavla Koštuříková
email: kosturikovap@gmail.com
discord: Pavla K
"""

# import funkcí ze souboru projekt_2_2_fce.py
from projekt_2_2_fce import grid
from projekt_2_2_fce import win
from projekt_2_2_fce import correct_input
from projekt_2_2_fce import occupied

# vytvoření prázdného pole
pole_piskvorek = []
for radek in range(3):
    for sloupec in range(3):
        pole_piskvorek.append(" ")

# úvodní text
print("Welcome to Tic Tac Toe")
print(cara_2 := "=" * 55)
print("GAME RULES:\nEach player can place one mark"
      " (or stone)\nper turn on the 3x3 grid. "
      "The WINNER is\nwho succeeds in placing "
      "three of their\n marks in a:\n"
      "* horizontal,\n* vertical or\n*diagonal row")
print(cara_2)
print("Let's start the game.")
print(cara_1 := "-" * 55)
grid(pole_piskvorek) # zobrazení prázdného pole
print(cara_2)


while " " in pole_piskvorek:
    # vstup od uživatele - hráč O
    player_O = input("Player O | Please enter your move number (1-9): ")
    player_O = correct_input(player_O, "O")    # kontrola správného vstupu hráče O
    player_O = occupied(player_O, pole_piskvorek, "O")    # kontola obsazenosti buňky

    print(cara_2)

    pole_piskvorek[player_O-1] = "O"    # označení znaku O do vybrané buňky
    grid(pole_piskvorek)    # zobrazení aktualizovaného pole

    print(cara_2)

    win(pole_piskvorek, "O")    # kontola výhry

    if " " not in pole_piskvorek:     # kontrola remízy
        print("It is a tie.")
        exit()

    # vstup od uživatele - hráč X
    player_X = input("Player X | Please enter your move number (1-9): ")
    player_X = correct_input(player_X, "X")    # kontola správného vstupu hráče X
    player_X = occupied(player_X, pole_piskvorek, "X")    # kontola obsazenosti buňky
    
    print(cara_2)

    pole_piskvorek[player_X-1] = "X"    # označení znaku X do vybrané buňky
    grid(pole_piskvorek)    # zobrazení aktualizovaného pole

    print(cara_2)

    win(pole_piskvorek, "X") # kontrola výhry

print(cara_2)