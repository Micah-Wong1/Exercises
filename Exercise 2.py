import random

"""
Nom: Micah Wong
Gr: 406
Ce code est la deuxieme exercise de POO
"""


def base_stat():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)
    dice_4 = random.randint(1, 6)

    die = [dice_1, dice_2, dice_3, dice_4]
    smallest_dice = die[0]

    for i in die:
        if i < smallest_dice:
            smallest_dice = i

    stat = dice_1 + dice_2 + dice_3 + dice_4 - smallest_dice
    return stat


print(base_stat())


class NPC:

    def __init__(self, nom, race, espece, metier):
        self.Force = base_stat()
        self.Agility = base_stat()
        self.Constitution = base_stat()
        self.Intelligence = base_stat()
        self.Sagesse = base_stat()
        self.Charisme = base_stat()
        self.Armure = random.randint(1, 12)
        self.Nom = nom
        self.Race = race
        self.Espece = espece
        self.HP = 20
        self.Profession = metier

    def afficher_caracteristiques(self):
        print(f"Nom = {self.Nom}")
        print(f"Espece = {self.Espece}")
        print(f"Race = {self.Race}")
        print(f"Profession = {self.Profession}")
        print(f"HP = {self.HP}")
        print(f"Force = {self.Force}")
        print(f"Agilité = {self.Agility}")
        print(f"Constitution = {self.Constitution}")
        print(f"Integlligence = {self.Intelligence}")
        print(f"Sagesse = {self.Sagesse}")
        print(f"Charisme = {self.Charisme}")
        print(f"Armure = {self.Armure}")


Civilian = NPC("Victor", "Asian", "Humain", "Scientifique")
Civilian.afficher_caracteristiques()
