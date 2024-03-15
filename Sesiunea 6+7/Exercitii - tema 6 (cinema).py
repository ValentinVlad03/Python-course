
"""
Creati o clasa cinema in care sa stocati atributele si metodele de care e nevoie ca sa puteti
sa gestiona un sistem de tip cinema (acestea vor fi implementate la alegerea voastra).
Clasa nu va avea constructor.

Creati cel putin 5 metode de test si 10 atribute.

Apelati pe rand fiecare dintre metodele create si respectiv printati  pe ecran toate valorile
atributelor pentru fiecare obiect. Printarea se va face cu formatare si, pentru o complexitate
mai mare, puteti sa puneti toate obiectele instantiate intr-o lista pe care sa o parcurgeti
cu un for (si astfel sa faceti printarea pentru toate elementele concomitent).
Repetati actiunea cu while si respectiv cu foreach. Rulati codul.

Modificati clasa prin adaugarea unui constructor care sa primeasca doi parametri care sa populeze,
la alegere, doua dintre atributele definite in clasa. Rulati codul. Ce observati?

Faceti modificarile necesare astfel incat sistemul sa nu mai returneze eroare.

Modificati constructorul astfel incat sa controlati valorile care sunt salvate in fiecare atribut.
Spre exemplu: daca se incearca salvarea numarului de locuri pentru cinema cu un numar mai mare
de 500, atunci sa se printeze pe ecran un mesaj de eroare.

Rulati codul din nou si introduceti o valoare care sa nu respecte conditia definita in constructor
(ex: un numar de locuri mai mare decat 500). Ce observati?

"""


class Cinema:
    def __init__(self, nume, adresa, capacitate):
        self.nume = nume
        self.adresa = adresa
        self.capacitate = capacitate
        self.ora_deschidere = 9
        self.ora_inchidere = 22
        self.pret_bilet = 25
        self.pret_popcorn = 15
        self.filme = []
        self._bilete_vandute = 0
        self.__total_incasari = 4000

    def add_film(self, film):
        self.filme.append(film)

    def remove_film(self, film):
        self.filme.remove(film)
        print(f'Am scos din program filmul: "{film}". ')

    def rulare_filme(self):
        print("Filmele care ruleaza la", self.nume, ":")
        for film in self.filme:
            print("    -", film)

    def vinde_bilete(self, numar_bilete_vandute):
        locuri_disponibile = self.capacitate - self._bilete_vandute
        if locuri_disponibile >= numar_bilete_vandute:
            self._bilete_vandute += numar_bilete_vandute
            print(f'Am vândut {numar_bilete_vandute} bilete.')
        else:
            print(f"Nu avem suficiente locuri libere pentru solicitarea Dvs.")


    def afisare_informatii(self):
        print(f'---------------------------------')
        print(  f'Nume : {self.nume}',
                f'\n Adresa : {self.adresa}',
                f'\n Capacitate : {self.capacitate} locuri',
                f'\n Program: {self.ora_deschidere} - {self.ora_inchidere}',
                f'\n Preţul biletului : {self.pret_bilet} lei',
                f'\n Preţul popcorn-ului : {self.pret_popcorn} lei'
                f'\n Număr bilete vândute : {self._bilete_vandute} bilete',
                f'\n Totalul de încasări: {self.__total_incasari} lei')
        print(f'---------------------------------')

# definim un cinema de la Mall AFI Cotroceni
cinema1 = Cinema("Cinema City", "str. Paul Teodorescu nr. 4, Sector 6, Bucureşti", 500)
cinema1.afisare_informatii()

# adaugam filme care sa ruleze la acest cinema
cinema1.add_film("Bordea: Teoria conspiratiei")
cinema1.add_film("Aquaman si Regatul pierdut")
cinema1.add_film("Haos in ajun de Craciun")
cinema1.add_film("Marea migratie")
cinema1.add_film("Napoleon")
cinema1.add_film("Scenariu de vis")
cinema1.rulare_filme()

# retragem un film din programul cinema-ului şi apoi afişăm noua listă de filme
cinema1.remove_film("Bordea: Teoria conspiratiei")
cinema1.rulare_filme()
print(f'---------------------------------')

# vindem bilete până se termină coada la ghişeu :))
locuri_disponibile = cinema1.capacitate - cinema1._bilete_vandute
print(f"Sala mai are {locuri_disponibile} locuri libere.")
numar_persoane_la_coada = int(input("Câte persoane sunt la coadă?  : "))
numar_client = 1
while numar_client <= numar_persoane_la_coada:
    if locuri_disponibile > 0:
        print(f'---------')
        print(f'Mai avem {locuri_disponibile} locuri libere.')
        print(f'Spectatorul nr. {numar_client} doreşte...')
        numar_bilete_dorite = int(input("Număr bilete: "))
        if numar_bilete_dorite <= locuri_disponibile:
            cinema1.vinde_bilete(numar_bilete_dorite)
            locuri_disponibile = locuri_disponibile - numar_bilete_dorite
        else:
            print(f'Nu avem disponibile atâtea locuri.')
    numar_client += 1
else:
    pass
if locuri_disponibile > 0:
    print(f'Au rămas {locuri_disponibile} locuri neocupate.')
else:
    print(f"Am epuizat toate biletele.")

# afişăm volumul de vânzări după ce am terminat de lucrat la ghişeu :)))
print(f"Numărul total de bilete vândute la {cinema1.nume} este: {cinema1._bilete_vandute}")
print(f"Preţul unui bilet este {cinema1.pret_bilet} lei.")
incasari = cinema1._bilete_vandute * cinema1.pret_bilet
print(f'Total încasări în sesiunea curentă: {incasari} lei.')


