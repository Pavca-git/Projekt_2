"""
projekt_2_1.py: druhý projekt do Engeto Online Python Akademie

author: Pavla Koštuříková
email: kosturikovap@gmail.com
discord: Pavla K
"""

# import funkcí ze souboru projekt_2_1_fce.py
import time
from projekt_2_1_fce import bull_cow
from projekt_2_1_fce import number_guesses
from projekt_2_1_fce import count_bull_cow
from projekt_2_1_fce import correct
from projekt_2_1_fce import generated_number
from projekt_2_1_fce import time_game

# úvodní text
print("Hi there!")
print(odd := "-" * 55)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(odd)

# vygenerování náhodného čísla pomocí funkce 'generated_number'
# a uložení do proměnné 'number'
number = generated_number()
print(f"PC generates a number: {number}")

# spuštění časomíry
start = time.time()

# vstup od uživatele a uložení do proměnné 'user'
user = input(f"Enter a 4 digit number:\n{odd}\n>>> ")

# počítání správných pokusů - proměnná 'count_guesses'
count_guesses = 1

# kontrola správnosti vstupu od uživatele pomocí funkce 'correct'
while not user.isnumeric() or len(user) != 4 or len(set(user)) != 4 or user[0] == "0":
    user = correct(user)

# výpočet počtu bull a cow pomocí funkce 'count_bull_cow'
# a zobrazení počtu bull a cow pomocí funkce 'bull_cow'
while user != number:
    count_guesses += 1
    bull = count_bull_cow(user, number)[0]
    cow = count_bull_cow(user, number)[1]
    bull_cow(bull, cow)
    print(odd)

    user = input(">>> ") # další vstup od uživatele
    # kontrola dalšího vstupu pomocí funkce 'correct'
    while not user.isnumeric() or len(user) != 4 or len(set(user)) != 4 or user[0] == "0":
        user = correct(user)

# konec časomíry
end = time.time()
print(odd)

# zobrazení počtu správných pokusů pomocí funkce 'number_guesses'
guesses = number_guesses(count_guesses)
print(f"Correct, you've guessed the right number in {guesses}!")

# zobrazení času hry pomocí funkce 'time_game'
timer = time_game(start, end)
print(f"Your game time is {timer}.")
print(odd)