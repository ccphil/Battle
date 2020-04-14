# imported classes ('Person', 'bcolor') from  'game.py'.
from classes.game import Person, bcolors


# Build a magic list filled with dictionaries.
magic = [
    {"name": "Fire", "cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 10, "dmg": 80},
    {"name": "Blizzard", "cost": 10, "dmg": 60},
]

# Next we instantiate the 'person' class named 'player' with hp, mp, atk, df, and magic spells.
player = Person(460, 65, 60, 34, magic)

# Next we instantaite the enemy. We are gonna reuse the 'Person' class that contains all the needed varaibles.
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0
# Using the 'bcolors' class we provide formating and color to the text. In order to limit the effect we need to end the statement with 'bcolors.ENDC'
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)


# Be careful this doesnt run indefinitly and cause stack overflow.
# Remember that in programming lists/arrays start at 0. in order to fix this we have to reduce our choice by 1 in oder to get spell nr 1.
while running:
    print("=========================================")
    # player.choose_action()
    player.choose_magic()
    choice = input("Choose action:")
    index = int(choice) - 1

    print("You chose", player.get_spell_name(int(index)))

    running = False
