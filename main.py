# imported classes ('Person', 'bcolor') from  'game.py'.
from classes.game import Person, bcolors


# Build a magic list filled with dictionaries.
magic = [
    {"name": "Fire", "cost": 10, "dmg": 100},
    {"name": "Thunder", "cost": 10, "dmg": 124},
    {"name": "Blizzard", "cost": 10, "dmg": 102},
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
# Remember that in programming lists/arrays start at 0. We want to choose starting at 1. in order to fix this we have to reduce our choice by 1 in oder to get spell nr 1.
while running:
    print("===========================================")
    player.choose_action()
    choice = input("Choose an action:")
    index = int(choice) - 1

    if index == 0:
        dmg = (
            player.generate_damage()
        )  # here we we assign the dmg parameter to the generatae_damage class which randomizes the dmg by choosing any number between our dmg low and dmg high.
        enemy.take_damage(dmg)  # telling the program who to assign the dmg to.
        print(
            "You attacked for", dmg, "points of damage."
        )  # Telling the player what is happening.
    elif index == 1:
        player.choose_magic()
        magic_choice = (
            int(input("Choose a spell:")) - 1
        )  # Here we reduce the choice by 1 already inline except doing it seperatly on a new line.
        # Get everything (information) we need from the spell.
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(
            magic_choice
        )  # variable 'spell' gets assigned the spell name by 'magic_choice"
        cost = player.get_spell_mp_cost(
            magic_choice
        )  # variable gets assigned the mana cost for spell.
        # Get infromation about players mana points and check if they are sufficent.
        current_mp = (
            player.get_mp()
        )  # Get current mana from player and put it into new variable

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(
            bcolors.OKBLUE + "\n" + spell + " deals",
            str(magic_dmg),
            "points of damage." + bcolors.ENDC,
        )

    enemy_choice = 1  # forcing the enemy to always choose 1.

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("-----------------------------------------")
    print(
        "Enemy HP:",
        bcolors.FAIL
        + str(enemy.get_hp())
        + "/"
        + str(enemy.get_max_hp())
        + bcolors.ENDC
        + "\n",
    )
    print(
        "Your HP:",
        bcolors.OKGREEN
        + str(player.get_hp())
        + "/"
        + str(player.get_max_hp())
        + bcolors.ENDC,
    )
    print(
        "Your MP:",
        bcolors.OKBLUE
        + str(player.get_mp())
        + "/"
        + str(player.get_max_mp())
        + bcolors.ENDC
        + "\n",
    )

    if enemy.get_hp() == 0:  # when enemy hits 0 hp
        print(
            bcolors.OKGREEN + "You win!" + bcolors.ENDC
        )  # Win statment gets printed in greeen color. (color also gets stopped)
        running = False  # program ends the while loop here (becauise we won)
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lost!" + bcolors.ENDC)
        running = False

if input(
    "exit"
):  # just for stopping the program while testing. buggy but seems to work.
    running = False

"""while running:
    print("=========================================")
    # player.choose_action()
    player.choose_magic()
    choice = input("Choose action:")
    index = int(choice) - 1

    print("You chose", player.get_spell_name(int(index)))

    running = False
"""
