

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Bc. Martin Novák
email: m.novak44@seznam.cz
"""
import re
# Texty pro analýzu

TEXTS = [
    '''
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.''',
]

# Uživatelé pro přihlášení
USERS = {
    "ann": "pass123",
    "bob": "123",
    "liz": "pass123",
    "mike": "password123",
}

# Přihlášení uživatele
print("username:")
username = input()
print("password:")
password = input()

if USERS.get(username) != password:
    print("Neregistrovaný uživatel nebo špatné heslo, konec programu.")
    exit()

print(f"Vítej v aplikaci, {username}")
print("Máme tři texty na analýzu.")
print("Zadej číslo textu mezi 1 až 3 pro analýzu:", end=" ")
vyber = input()

if not vyber.isdigit() or int(vyber) not in {1, 2, 3}:
    print("Neplatná volba, konec programu.")
    exit()

print("-" * 40)
text = TEXTS[int(vyber) - 1]

# Rozdělení textu na slova a odstranění interpunkce
words = text.split()
cleaned_words = [re.sub(r'[^\w]', '', word) for word in words if word.strip() != '']

# Počítání různých typů slov
titlecase = sum(1 for word in cleaned_words if word.istitle())
uppercase = sum(1 for word in cleaned_words if word.isupper() and word.isalpha())
lowercase = sum(1 for word in cleaned_words if word.islower())
numeric = [int(word) for word in cleaned_words if word.isdigit()]

print(f"Ve vybraném textu je {len(cleaned_words)} slov.")
print(f"Ve vybraném textu je {titlecase} titlecase slov.")
print(f"Ve vybraném textu je {uppercase} uppercase slov.")
print(f"Ve vybraném textu je {lowercase} lowercase slov.")
print(f"Ve vybraném textu je {len(numeric)} numeric strings.")
print(f"Součet všech čísel je {sum(numeric)}")
print("-" * 40)

# Počítání délky slov a jejich výskytu
delka_slov = {}
for word in cleaned_words:
    length = len(word)
    if length > 0:
        delka_slov[length] = delka_slov.get(length, 0) + 1

print("LEN|  OCCURENCES  |NR.")
print("-" * 40)
for length in sorted(delka_slov):
    stars = '*' * delka_slov[length]
    print(f"{length:>3}|{stars:<15}|{delka_slov[length]}")

input("Stiskněte Enter pro ukončení programu...")

print("Program byl ukončen.")
