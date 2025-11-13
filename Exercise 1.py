from math import pi

"""
Nom: Micah Wong
Gr: 406
Ce code est la premiere exercise
"""

#exercise 1

class Stringfoo:

    def __init__(self):
        self.message = ""

    def set_string(self, message):
        self.message = message

    def print_string(self):
        print(self.message.upper())


reponse = str(input("Entrez votre phrase:"))

string1 = Stringfoo()
string1.set_string(reponse)
string1.print_string()

#exercise 2

class Rectangle:

    def __init__(self, longeur, largeur):
        self.longeur = longeur
        self.largeur = largeur
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.longeur * self.largeur

    def affiche_infos(self):
        print(f"L'aire du rectangle est de {self.aire}")
        print(f"avec une longeur de {self.longeur} et une largeur de {self.largeur}")


base = int(input("Quel est le longeur du rectangle?"))
hauteur = int(input("Quel est le largeur du rectangle?"))

rectangle1 = Rectangle(base, hauteur)
rectangle1.calcul_aire()
rectangle1.affiche_infos()

#exercise 3

class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon
        self.aire_cir = 0
        self.circ = 0

    def calcul_aire_cir(self):
        self.aire_cir = pi * self.rayon * self.rayon
        print(f"L'aire du cercle est de {self.aire_cir}")

    def calcul_circonferance(self):
        self.circ = 2 * pi * self.rayon
        print(f"Le circonferance du cercle est {self.circ}")


r = int(input("Quel est le rayon du cercle?"))
circle = Cercle(r)
circle.calcul_aire_cir()
circle.calcul_circonferance()

#exercise 4

class Hero:

    def __init__(self, nom, hp, attaque, defense):
        self.name = nom
        self.HP = hp
        self.atk = attaque
        self.blk = defense

    def faire_attaque(self):


superman = Hero("Clark", 10, 5, 6)
