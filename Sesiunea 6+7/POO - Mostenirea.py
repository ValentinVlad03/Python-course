
# MOŞTENIREA
"""
MOŞTENIREA este un concept in POO care permite unei clase copil (numită clasă derivată sau subclasă)
să preia atribute şi metode de la una sau mai multe clase părinte (numită şi clasa de bază sau superclasă).

Clasa copil preia atributele şi metodele clasei părinte şi poate adăuga sau modifica comportamentul acesteia.
Avantajul moştenirii este că nu mai este nevoie să scriem acelaşi cod de mai multe ori.
O clasă copil poate să moştenească un număr nelimitat de clase părinte.

"""

# exemplu de definire a clasei părinte şi clasei copil.

class Animal:
    def __init__(self, nume):   # Aceasta este clasa de baza (parinte) in ierarhia de mostenire.
        self.nume = nume

    def sunet(self):            # aici avem o metoda cu implementare implicita
        return "Sunet necunoscut."

class Caine(Animal):            # clasa copil care mosteneste clasa parinte "Animal"
    def sunet(self):            # aceasta metoda va suprascrie metoda din clasa parinte
        return "Ham, ham!"

class Pisica(Animal):
    def sunet(self):
        return "Miau, miau!"

rex = Caine(nume = "Rex")
tom = Pisica(nume = "Tom")

print(rex.nume)
print(tom.nume)
print(rex.sunet())
print(tom.sunet())


# --------------------------------------------------------------------
# Exemplu de mostenire multipla

class AnimalTerestru:
    def deplasare(self):
        return "Se deplaseaza pe uscat."

class AnimalAerian:
    def deplasare(self):
        return "Se deplaseaza in aer."

class Pasare(AnimalAerian, AnimalTerestru):
    pass

papagal = Pasare()
print(papagal.deplasare())


