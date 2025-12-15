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


class NPC:

    def __init__(self):
        self.Force = base_stat()
        self.Agility = base_stat()
        self.Constitution = base_stat()
        self.Intelligence = base_stat()
        self.Sagesse = base_stat()
        self.Charisme = base_stat()
        self.Armure = random.randint(1, 12)
        self.Nom = ""
        self.Race = ""
        self.Espece = ""
        self.HP = 20
        self.Profession = ""

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


class Kobold(NPC):

    def __init__(self):
        super().__init__()

    @staticmethod
    def attaquer(cible):
        power = random.randint(1, 20)
        if power == 1:
            pass
            print("Attaque raté...")
        elif power == 20:
            cible.subir_dommages(8)
            print("ATTAQUE CRITIQUE!!")
        else:
            if power >= cible.Armure:
                cible.subir_dommages(6)
                print("Attaque normal!")
            else:
                pass
                print("Attaque raté...")
        print(f"Health left: {cible.HP}")

    def subir_dommages(self, dmg):
        self.HP = self.HP - dmg


class Hero(NPC):
    def __init__(self):
        super().__init__()

    @staticmethod
    def attaquer(cible):
        power = random.randint(1, 20)
        if power == 1:
            pass
            print("Attaque raté...")
        elif power == 20:
            cible.subir_dommages(8)
            print("ATTAQUE CRITIQUE!!")
        else:
            if power >= cible.Armure:
                cible.subir_dommages(6)
                print("Attaque normal!")
            else:
                pass
                print("Attaque raté...")
        print(f"Health left: {cible.HP}")

    def subir_dommages(self, dmg):
        self.HP = self.HP - dmg


boss_1 = Kobold()
boss_1.Nom = "Verka"
boss_1.Race = "Kobold Bleu"
boss_1.Espece = "Koblod"
boss_1.Profession = "Villan"
boss_1.afficher_caracteristiques()
superman = Hero()
superman.Nom = "Clark"
superman.Race = "Kryptonian"
superman.Espece = "Kryptonian"
superman.Profession = "Hero"
superman.afficher_caracteristiques()
superman.attaquer(boss_1)
boss_1.attaquer(superman)
