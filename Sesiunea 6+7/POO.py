"""
POO / OOP - Programarea Orientata pe Obiecte (Object Oriented Programming)

POO este o modalitate prin care putem sa structuram proprietatile si comportamentul unei
entitati din viata reala intr-o structura logica ce functioneaza ca un template (sablon).
Acest template va servi drept model pentru crearea unei entitati care să reprezinte un
exemplu din viaţa reală.

POO se bazează pe clase şi obiecte.

O clasă este un şablon sau un model (ca o reţetă) pentru a crea obiecte. Ea defineşte
atributele şi modelele care vor fi prezente în obiectele create din acea clasă.

Obiectele sunt instanţe ale claselor. Acestea conţin date specifice (atribute) şi se pot
apela metodele definite in clasa lor.

Atributele sunt variabile definite într-o clasă. Atributele unei clase descriu cum ar
trebui să arate entitatea (= ce proprietăţi să aibe).

Metodele sunt funcţii definite într-o clasă, Metodele unei clase descriu ce ar trebui să
facă entitatea (= cum să se comporte).

Diferenţa dintre funcţii şi metode ....
"""

# exemplul 1.

class Masina:
    def __init__ (self, marca, model):
        self.marca = marca
        self.model = model

    def afiseaza_informatii(self):
        print(f"Masina: {self.marca} {self.model}")

# exemplul de obiect al clasei Masina

masina_mea = Masina(marca = "Dacia", model = "Duster")
print(masina_mea.marca, masina_mea.model)
masina_mea.afiseaza_informatii()


# ------------------------------------------------------------------------------

# ex. 2

class Caine:                            # aici am definit clasa Caine
    def __init__(self, nume, varsta):   # am definit metoda speciala __init__ care actioneaza ca un constructor
        self.nume = nume                # am definit atributele nume si varsta ale obiectului, ce sunt
                                        # initializate cu valorile primite la crearea obiectului
        self.varsta = varsta

    def latra(self):                    # am definit metoda "latra" care afisează un mesaj simplu în consolă
        print("Ham, ham!")


# definim un obiect al clasei Caine

rex = Caine(nume= "REX", varsta= 3)     # am creat un obiect "REX"
print(rex.nume)                         # se accesează şi se afişează valorile atributului nume
print(rex.varsta)
rex.latra()                             # am apelat metoda latră a obiectului rex. Se va afişa "ham, ham!"

"""
Există două tipuri de constructori: 
1. Constructor implicit = care este incorporat in limbajul Python si el este apelat automat cand nu există
un constructor explicit.

2. Constructor explicit = este definit de către un utilizator .....
"""

# #xemplu de constructor implicit
class Masina:
    def __init__(self):
        self.model = "Nissan"
        self.an_fabricatie = 2020

    def afisare_informatii(self):
        print(f"Model: {self.model}, an_fabricatie: {self.an_fabricatie}")

masina1 = Masina()
masina1.afisare_informatii()


# exemplu de constructor explicit

class Masina:
    def __init__(self, model = "Dacia", an_fabricatie = 2020):
        self.model = model
        self.an_fabricatie = an_fabricatie

    def afisare_informatii(self):
        print(f"Model: {self.model}, an fabricatie: {self.an_fabricatie}")

masina2 = Masina(model="Tesla", an_fabricatie=2022)
masina2.afisare_informatii()


# ex. cu constructor explicit

class Scoala():
    # atribute pe care le poate avea scoala
    adresa = None           # am pus "None" pentru ca fiecare obiect al clasei să poată avea propria adresă
    ciclu_invatamant = "Primar"
    capacitate_elevi = None
    numar_profesori = None
    profil = "Real"
    clase = {}              # este un dictionar care va contine informatii despre clasele scolii

    # mai jos definim un constructor explicit
    def __init__(self, adresa, ciclu_invatamant, profil):
        self.adresa = adresa
        self.ciclu_invatamant = ciclu_invatamant
        self.profil = profil
        while profil.lower() not in ("real", "uman"):
            profil = input("Profil invalid. Va rugam sa introduceti una din optiunile: 'real' sau 'uman'.")

    # definim activitatile care se pot face intr-o scoala
    def adauga_clasa(self, nume_clasa, profil, ciclu, numar_elevi, numar_profesori):
        self.clase[nume_clasa] = {"profil": profil,
                                  "ciclu": ciclu,
                                  "numar elevi": numar_elevi,
                                  "numar profesori": numar_profesori}

    # definim o metoda pentru actualizarea adreselor
    def actualizare_adresa_scoala(self, adresa_noua):
        self.adresa = adresa_noua
        print(self.adresa)
        return self.adresa          # returneaza noua adresa astfel incat sa poata fi utilizata sau afisata  in alta parte a codului

    # defim o metoda care sa extraga numarul de profesori
    def extrage_numarul_de_profesori(self):
        return self.numar_profesori    # returneaza valoarea atributului numar_profesori al obiectului curent

                        # atunci cand intantiem un obiect dintr-o clasa cu constructor explicit suntem
                        # obligati sa dam valori pentru parametri definiti in constructorul explicit.
                        # Aceasta instantiere o sa genereze eroare pentru ca incercam sa instantiem un obiect
                        # fara sa ii dam valori pentru parametri din constructor.

    scoala1 = Scoala(adresa = "Strada Mihai Voda nr. 23.", ciclu_invatamant = "primar", profil = "Uman")
    print(f"Adresa scolii este: {scoala1.adresa}")
    print(f"Ciclul de invatamant : {scoala1.ciclu_invatamant}")
    print(f"Profilul este:  {scoala1.profil}")

    scoala2 = Scoala(adresa = "Strada Lunguletu nr. 6", ciclu_invatamant = "primar", profil = "Teoretic")
    print(f"Profilul este: {scoala2.profil}")

    scoala1.actualizare_adresa_scoala("Strada Mircea cel Batran nr. 30")
    print(scoala1)      # printeaza adresa de memorie care reprezinta obiectul
    print(f"Noua adresa este: {scoala1}")

    scoala1.numar_profesori = 45
    print(scoala1.extrage_numar_de_profesori())

# sa printam atributele definite la nivel de clasa
print(f"Atributele definite la nivel de clasa sunt: {scoala1.adresa} {scoala1.profil} "
      f" {scoala1.numar_profesori} {scoala1.ciclu_invatamant} {scoala1.clase}")

# sa printam atributele definite la nivel de obiect
print(f"Atributele definite la nivel de obiect sunt: {Scoala.adresa} {Scoala.profil} {Scoala.clase}"
      f" {Scoala.numar_profesori} {Scoala.ciclu_invatamant} {Scoala.capacitate_elevi}")

# ATENTIE!!! Ordinea argumentelor date la instantiere trebuie
# sa coincida cu ordinea parametrilor definiti in constructor!

scoala3 = Scoala(adresa = "Strada Margelelor nr. 60", ciclu_invatamant = "Gimnazial", profil = "Real")
print(f"Atributele definite la nivel de obiect 'scoala3' sunt: "
      f"{scoala3.adresa} {scoala3.ciclu_invatamant} {scoala3.profil}")


# -------------------------------------------------------------------------------

"""
In POO exista patru principii principale:
1. Moştenirea (inheritance)
2. Abstractizarea (abstracting)
3. Polimorfism (polymorphism)
4. Incapsularea (incapsulation)


"""