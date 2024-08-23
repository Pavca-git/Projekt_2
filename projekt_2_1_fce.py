"""
projekt_2_1_fce.py: funkce pro druhý projekt do Engeto Online Python Akademie

author: Pavla Koštuříková
email: kosturikovap@gmail.com
discord: Pavla K
"""

import random

# funkce pro vygenerování náhodného čísla bez duplicit
def generated_number():
    number_set = set()
    while len(number_set) != 4:
        num = str(random.randint(1,9))
        number_set.add(num)
    number_list = list(number_set)
    number = "".join(number_list)
    return number



# funkce pro kontrolu správnosti vstupu
def correct(user):
    if not user.isnumeric():
        print("Incorrect input!\nInput must not contain letters!")
    elif len(user) != 4:
        print("Incorrect input!\nInput must contain 4 digits!")
    elif len(set(user)) != 4:
        print("Incorrect input!\nInput must not contain duplicate digits!")
    elif user[0] == "0":
        print("Incorrect input!\nInput must not start with zero!")
    user = input("Please enter a 4 digit number again:\n>>> ")        
    return user

# funkce pro výpočet počtu cow a bull
def count_bull_cow(user, number):
    num_index = 0
    bull = 0
    cow = 0
    for index in user:
        if str(index) == number[num_index]:
            bull += 1
        elif str(index) != number[num_index] and str(index) in list(number):
            cow += 1
        num_index += 1
    return bull, cow


# funkce pro zobrazení počtu cow a bull
def bull_cow(bull, cow):
    if bull <= 1:
        listing_bull = f"{bull} bull"
    else:
        listing_bull = f"{bull} bulls"
    
    if cow <= 1:
        listing_cow = f"{cow} cow"
    else:
        listing_cow = f"{cow} cows"
    
    return print(f"{listing_bull}, {listing_cow}")


# funkce pro zobrazení počtu pokusů - při správných vstupech uživatele
def number_guesses(count_guesses):
    if count_guesses == 1:
        word = "guess"
    else:
        word = "guesses"
    return f"{count_guesses} {word}"

# funkce pro zobrazení času hry - hodiny, minuty, sekundy
def time_game(start, end):
    time = end - start
    if time < 60:
        s = round(time, 2)
        format_time = (f"{s} s")
    elif 3600 > time >= 60:
        m = int(time / 60)
        s = round((time % 60), 2)
        format_time = (f"{m} min {s} s")
    else:
        h = int(time / 3600)
        m = int(time % 60)
        s = round(((time % 3600) % 60), 2)
        format_time = (f"{h} h {m} min {s} s")
    return format_time