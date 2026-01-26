from enum import Enum
from dataclasses import dataclass
import random

"""
Nom: Micah Wong
Gr: 406
Ce code est la troisieme exercise de TP4
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


class Alignments(Enum):
    lawful_good = 1
    lawful_neutral = 2
    lawful_evil = 3
    neutral_good = 4
    true_neutral = 5
    neutral_evil = 6
    chaotic_good = 7
    chaotic_neutral = 8
    chaotic_evil = 9
    undefined = 10


class NPC:

    def __init__(self):
        self.Force = base_stat()
        self.Agility = base_stat()
        self.Constitution = base_stat()
        self.Intelligence = base_stat()
        self.Sagesse = base_stat()
        self.Charisme = base_stat()
        self.Alignment = Alignments(random.randint(1, 10))
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


@dataclass
class Item:

    nom_item: str
    quantite_item: int


class Inventory:

    def __init__(self):
        self.items = []

    def ajouter_item(self, item_added: Item):
        item_found = False
        if len(self.items) <= 0:
            self.items.append(item_added)
        else:
            for item in self.items:
                if item.nom_item == item_added.nom_item:
                    item.quantite_item += item_added.quantite_item
                    item_found = True
            if not item_found:
                self.items.append(item_added)

    def retirer_item(self, nom_item, quantite_item):
        item_trouve = False
        if len(self.items) <= 0:
            return

        for item in self.items:
            if item.nom_item == nom_item:
                item_trouve = True
                if item.quantite_item - quantite_item < 0:
                    print("Erreur: quantité insuffisante")
                    return
                elif item.quantite_item - quantite_item == 0:
                    self.items.remove(item)
                else:
                    item.quantite_item -= quantite_item
        if not item_trouve:
            print("Erreur: Item non-trouve")

    def voir_contenu(self):
        print(self.items)


inv = Inventory()
inv.ajouter_item(Item("Stylo", 1))
inv.ajouter_item(Item("Stylo", 2))
inv.ajouter_item(Item("Ruler", 1))
inv.retirer_item("Stylo", 2)
inv.retirer_item("Ruler", 2)
inv.retirer_item("nothing", 1)
inv.voir_contenu()


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

    def vivant(self):
        if self.HP > 0:
            print(f"Health: {self.HP}")
        elif self.HP <= 0:
            print("Health: 0")


class Hero(NPC):
    def __init__(self):
        super().__init__()
        self.inven = Inventory()

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

    def vivant(self):
        if self.HP > 0:
            print(f"Health: {self.HP}")
        elif self.HP <= 0:
            print("Health: 0")

    def subir_dommages(self, dmg):
        self.HP = self.HP - dmg
