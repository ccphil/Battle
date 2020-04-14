# we start by defining by classes.
# We want colours in terminal
import random


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp  # tells us what our MAX hitpoints are.
        self.hp = hp  # tells us what CURRENT hitpoints are.
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10  # Attack low
        self.atkh = atk + 10  # Attack high
        self.df = df
        self.magic = magic  # 'magic' object will be a dictionary of different magic spells with their associated mana costs.
        self.action = ["Attack", "Magic"]  # Displaying what we can do every turn.

    # Function to create random dmg, to make it more dynamaic.
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # next are some utility classes defined.
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):  # this function takes 'cost' as a parameter.
        self.mp -= cost  # dont need to return anything

    def get_spell_name(self, i):  # pass it an index number
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.action:
            print(str(i) + ":", item)  # pint index number to string.
            i += 1  # going to increment i

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(
                str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")"
            )  # convert indexnr. to str and glue it together with the spell.
            i += 1


"""    def choose_magic(self):
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print(" " + str(i) + ":", spell.["name"], "(cost:", str(spell.cost) + ")")
            i += 1"""
