"""
Incapsularea = este posibilitatea de a restrictiona accesul la anumite atribute si metode dintr-o clasa
astfel incat sa protejam datele, să arătăm utilizatorului doar informaţiile de care are nevoie.
Motivul pentru care vrem să facem asta este fie din motive de securitate, fie pentru a controla modificarea
de către utilizator.

Există trei tipuri:
a) public (fără restricţii) = atributul sau metoda sunt accesibile oriunde în program
b) private = atributele şi metodele sunt accesibile doar în interiorul clasei în care au fost definite.
   Vor fi precedate de caracterele "__"
c) protected = atributele şi metodele sunt vizibile oriunde dar nu sunt returnate ca sugestii.
   Vor fi precedate de caracterul "_"

"""

# Ex.  a) Public

class ExempluPublic:
    def __init__(self):
        self.public_var = 10


obiect = ExempluPublic()
print(obiect.public_var)



# Ex.  b) Privat

# class ExempluPrivat:
#     def __init__(self):
#         self.__privat_var = 30
#
# obiect1 = ExempluPrivat()
# print(obiect1.__privat_var)         # acesta va genera o eroare



# Ex.  c) Protected

class ExempluProtejat:
    def __init__(self):
        self._protejat_var = 20

obiect2 = ExempluProtejat()
print(obiect2._protejat_var)

# Atunci cand avea de-a face cu atribute private (mai ales) sau protected, de regula, se definesc ceea
# ce se numeste:
#       - getter = metoda pentru extragerea valorii din atribut
#       - setter = metoda pentru actualizarea valorii din atribut
#       - deleter = metoda pentru stergerea valorii din atribut


class Cinema:
    def __init__(self, nume, adresa, capacitate):
        self.nume = nume
        self.adresa = adresa
        self.capacitate = capacitate
        self.filme = []
        self._bilete_vandute = 0    # am definit atributul ca fiind protected folosind caracterul "_"
        self.__total_incasari = 5000    # am definit atributul ca fiind privat
        self.faliment = False

    def add_film(self, film):
        self.filme.append(film)

    def remove_film(self, film):
        self.filme.remove(film)

    def rulare_film(self):
        print("Filmele ruleaza la ", self.nume, ' cinema.')
        for film in self.film:
            print(" - ", film)

    def vinde_bilete(self, numar_bilete_vandute):
        self._bilete_vandute += numar_bilete_vandute

    @property
    def total_incasari(self):
        pass

    @total_incasari.getter
    def total_incasari(self):
        return self.__total_incasari

    @total_incasari.setter
    def total_incasari(self, valoare_modificare_total):
        self.__total_incasari += valoare_modificare_total

    @total_incasari.deleter
    def total_incasari(self):
        self.__total_incasari = 0


cinema_afi = Cinema('Hollywood', 'Parklake', 150)
print(f"Filmele care ruleaza la cinema AFI sunt: {cinema_afi.filme}")
print(f"La cinema AFI s-au vandut: {cinema_afi._bilete_vandute}")
# print(cinema_afi.__total_incasari)
cinema_afi.floricele = 50               # aici cream un atribut nou specific doar obiectului cinema_afi, acesta nu poate fi folosit de alte obiecte.
print(cinema_afi.floricele)
cinema_plaza = Cinema('Bolywood', 'Plaza Romania', 250)
# print(cinema_plaza.floricele)

# Apelare getter:
print(f"Incasarile accesate prin getter: {cinema_afi.total_incasari}")   # Atentie! Nu se mai pun cele 2 paranteze rotunde!

# Apelare setter:
cinema_afi.total_incasari = 61
print(f"Incasarile accesate prin setter: {cinema_afi.total_incasari}")    # Atentie! Nu se mai pun cele 2 paranteze rotunde!

# Apelare deleter:
del cinema_afi.total_incasari
print(f"Incasarile accesate prin deleter: {cinema_afi.total_incasari}")    # Atentie! Nu se mai pun cele 2 paranteze rotunde!