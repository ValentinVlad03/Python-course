"""
Sa creati un mini proiect care sa implementeze cei patru piloni ai programarii:


ABSTRACTIZARE
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’


MOSTENIRE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură


ENCAPSULARE
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)


POLYMORFISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Pătrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

"""


# MOSTENIREA
class SistemOperare:
    def __init__(self,telefon):
        self.telefon = telefon

class Android(SistemOperare):
    def so(self):
        return "Sistemul de operare al telefonului este Android!"

class iOS(SistemOperare):
    def so(self):
        return "Sistemul de operare al telefonului este iOS!"

motorola = Android(telefon="Samsung")
iphone = iOS(telefon="Apple iPhone")
print(" - Motorola >>> ", motorola.so())
print(" - iPhone   >>> ", iphone.so())


# POLIMORFISMUL

class XiaomiPocoF5:
    def tip_telefon(self):
        return "Acesta este un telefon cu Android."

class MotorolaEdge40:
    def tip_telefon(self):
        return "Acesta este un telefon cu iOS."
def afiseaza_tip_telefon(telefoane):
    print(telefoane.tip_telefon())

xiaomi = XiaomiPocoF5()
apple_iphone = MotorolaEdge40()

afiseaza_tip_telefon(xiaomi)
afiseaza_tip_telefon(apple_iphone)


# ABSTRACTIZAREA

from abc import ABC, abstractmethod
class SistemeOperare(ABC):
    def __init__(self, versiune, an_lansare):
        self.versiune = versiune
        self.an_lansare = an_lansare
    @abstractmethod
    def detalii(self):
        pass

class Android(SistemeOperare):
    def detalii(self):
        print("Versiune SO: ", self.versiune);
        print("An lansare: ",self.an_lansare);

    def antivirus(self):
        print("Nu are aceasta optiune!")

class iOS(SistemeOperare):
    def detalii(self):
        print("Versiune SO: ", self.versiune);
        print("An lansare: ", self.an_lansare);

    def antivirus(self):
        print("Are aceasta optiune!")

print(f"...")
print(f"----------Samsung S21-----------")
SamsungS21 = Android("13", "2022")
SamsungS21.detalii()
SamsungS21.antivirus()
print(f"...")
print(f"---------iPhone 15 Pro------------")
iPhone15Pro = iOS("17", "2023")
iPhone15Pro.detalii()
iPhone15Pro.antivirus()
print(f"---------------------")


# INCAPSULAREA

class Android:
    def __init__(self, versiune, an_lansare):
        self.versiune = versiune
        self.an_lansare = an_lansare
        self.telefon = []
        self._unitatiVandute = 0
        self.__totalUnitati = 3000000

    def adaugare_telefon(self, telefon):
        self.telefon.append(telefon)

    def stergere_telefon(self, telefon):
        self.telefon.remove(telefon)

    def nr_unitati_vandute(self, nr_unitati_vandute):
        self._unitatiVandute += nr_unitati_vandute

    @property
    def totalUnitati(self):
        pass

    @totalUnitati.getter
    def totalUnitati(self):
        return self.__totalUnitati

    @totalUnitati.setter
    def totalUnitati(self, total_modificat):
        self.__totalUnitati += total_modificat

    @totalUnitati.deleter
    def totalUnitati(self):self.__totalUnitati = 0


Samsung = Android("13", "2022")
print(f'Modelul telefonului cu Android este: {Samsung.telefon}')
print(f'Numarul de unitati vandute este: {Samsung._unitatiVandute}')

#GETTER
print(f'Totalul unitatilor vandute apelate prin GETTER: {Samsung.totalUnitati}')

#SETTER
Samsung.totalUnitati = 23000
print(f'Totalul unitatilor vandute apelate prin SETTER: {Samsung.totalUnitati}')

#DELETER
del Samsung.totalUnitati
print(f'Totalul unitatilor vandute apelate prin DELETER: {Samsung.totalUnitati}')


