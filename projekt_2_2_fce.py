"""
projekt_2_2_fce.py: funkce pro druhý projekt do Engeto Online Python Akademie

author: Pavla Koštuříková
email: kosturikovap@gmail.com
discord: Pavla K
"""

# funkce pro zobrazení pole
def grid(pole):
    pole_list = [pole[:3], pole[3:6], pole[6:]]
    for radek in pole_list:
        print("+---+---+---+")
        print("", end="| ")
        for cislo in radek[0:2]:
            print(cislo, sep= " | ", end=" | ")
        for cislo in radek[2]:
            print(cislo, end=" | \n")
    print("+---+---+---+")

# funkce pro zjištění výhry
def win(pole, O_X):
    pole_list = [pole[:3], pole[3:6], pole[6:]]
    for radek in range(3):
        if pole_list[radek][0] == pole_list[radek][1] == pole_list[radek][2] == O_X:
            return print(f"Player {O_X} wins!") + exit()
    for sloupec in range(3):
        if pole_list[0][sloupec] == pole_list[1][sloupec] == pole_list[2][sloupec] == O_X:
            return print(f"Player {O_X} wins!") + exit()
    if pole_list[0][0] == pole_list[1][1] == pole_list[2][2] == O_X:
        return print(f"Player {O_X} wins!") + exit()
    if pole_list[2][0] == pole_list[1][1] == pole_list[0][2] == O_X:
        return print(f"Player {O_X} wins!") + exit()        


# funkce pro kontrolu správného vstupu
def correct_input(player, O_X):
    while not player.isnumeric() or int(player) < 1 or int(player) > 9:
        print("Not correct input. Try again.")
        player = input(f"Player {O_X} | Please enter your move number (1-9): ")
    return int(player)

# funkce pro kontrolu obsazenosti buňky
def occupied(player, pole_piskvorek, O_X):
    while " " not in pole_piskvorek[player-1]:
        print("This field is occupied!")
        player = input(f"Player {O_X} | Please enter your move number (1-9): ")
        while not player.isnumeric() or int(player) < 1 or int(player) > 9:
            print("Not correct input. Try again.")
            player = input(f"Player {O_X} | Please enter your move number (1-9): ")
        player = int(player)
    return player

