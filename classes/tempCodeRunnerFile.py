    def choose_magic(self):
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print(
                "        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")"
            )
            i += 1"""