# imported classes ('Person', 'bcolor') from  'game.py'.
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")
# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")
# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Haels 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals for 500", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
megaelixir = Item("MegaElixir", "elixir", "Fully restores HP/MP of entire party", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hipotion, superpotion, elixir, megaelixir, grenade]
# Instantiate Person
# Next we instantiate the 'person' class named 'player' with hp, mp, atk, df, and magic spells.
player = Person(
    460, 65, 60, 34, player_spells, player_items
)  # creating spell list inline marked by []

# Next we instantaite the enemy. We are gonna reuse the 'Person' class that contains all the needed varaibles.
enemy = Person(1200, 65, 45, 25, [], [])
# To recap we instantiate the Person class twice. One instance of the person class geos into player, the other into enemy. Using two different variables lets us use different parameters for the variables we set in the class.


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

    # Setting index 0 to be the attack option
    if index == 0:
        dmg = (
            player.generate_damage()
        )  # here we we assign the dmg parameter to the generatae_damage class which randomizes the dmg by choosing any number between our dmg low and dmg high.
        enemy.take_damage(dmg)  # telling the program who to assign the dmg to.
        print(
            "You attacked for", dmg, "points of damage."
        )  # Telling the player what is happening.
    # Setting index 1 to be the magic option
    elif index == 1:
        player.choose_magic()
        magic_choice = (
            int(input("Choose a spell:")) - 1
        )  # Here we reduce the choice by 1 already inline except doing it seperatly on a new line.

        # Get everything (information) we need from the spell.

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        # Get infromation about players mana points and check if they are sufficent.
        current_mp = (
            player.get_mp()
        )  # Get current mana from player and put it into new variable

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(
                bcolors.OKBLUE + "\n" + spell.name + "heals for",
                str(magic_dmg),
                "HP." + bcolors.ENDC,
            )
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(
                bcolors.OKBLUE + "\n" + spell.name + " deals",
                str(magic_dmg),
                "points of damage." + bcolors.ENDC,
            )
        if magic_choice == -1:
            continue
    # Setting index 2 to the inventory option
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose an item:")) + 1

    if item_choice == -1:
        continue

    enemy_choice = 1  # forcing the enemy to always choose attack (1.).

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
