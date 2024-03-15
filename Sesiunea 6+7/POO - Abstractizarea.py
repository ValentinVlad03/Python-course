"""
ABSTRACTIZAREA = implica izolarea unei entitati pentru a evidentia doar caracteristicile relevante
si a ascunde detaliile de implementare.
Reprezinta crearea a ceea ce putem numi un tipar pentru celelalte clase, astfel incat oricare clasa
care va veni si va mosteni clasa abstracta va fi obligata sa implementeze metodele abstracte definite
in acea clasa.
Daca noi marcam o metoda ca fiind abstracta si nu implementam in clasa copil vom primi o eroare
de tip "TypeError".
a) clase abstracte (ABC) - sunt clasele care nu pot fi instantiate direct si pot contine metode
normale si metode abstracte
b) metode abstracte (@abstractmethod) -  sunt definite in clasele abstracte, dar nu au implementare.
Acestea sunt implementate in clasele copil.

"""

# Ex.:  Metoda abstracta

from abc import ABC, abstractmethod

class Parinte(ABC):
    @abstractmethod
    def metoda_abstracta(self):
        pass

class Copil(Parinte):
    def metoda_abstracta(self):
        print("Implementare a metodei abstracte.")

copil = Copil()
copil.metoda_abstracta()

class Gradinita(ABC):
    @abstractmethod
    def joaca(self):
        raise NotImplementedError

    def somn(self):
        pass

    @abstractmethod
    def activitati(self):
        pass

class Gradinita_privata(Gradinita):
    nr_copil = 0
    adresa = None
    orar = None

    def joaca(self):
        print("Copiii alearga!")

    def activitati(self):
        print("Copiii coloreaza!")


class Gradinita_publica(Gradinita):
    nr_copil = 0
    adresa = None
    orar = None

    def joaca(self):
        print("Copiii sar coarda!")

    def activitati(self):
        print("Copiii canta!")

privata =  Gradinita_privata()
print(privata)
privata.joaca()
privata.activitati()
privata.somn()


publica = Gradinita_publica()
print(publica)
publica.joaca()
publica.activitati()
