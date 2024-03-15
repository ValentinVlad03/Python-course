# import math
#
#
# # FUNCTIILE
# # functiile sunt blocuri de cod reutilizabile care efectueaza o anumita actiune.
# # Ele sunt definite cu scopul de a limita numarul de linii de cod pe care le scriem
# # si de a face programul sa fie mai modular si respectiv mai usor de citit.
#
# # Componentele unei functii sunt:
# #    -- inceputul functiei definit prin "def"
# #    -- numele functiei, care nu trebuie sa fie un cuvant rezervat si se foloseste
# #        formatul snake_case
# #    -- parantezele rotunde in care se pot stoca parametri functiei
# #    -- separatorul intre lista de parametri si corpul functiei este ":"
# #    -- corpul functiei = setul de instructiuni care se vor executa la apelarea functiei
# #    -- (optional) functia de return
#
#
#
# # Exemplu:
# def salutare():     # definirea functiei
#     print("Salut!")
#
# salutare()      # apelul functiei
#
#                 # ca sa folosim instructiunile salvate intr-o functie
#                 # trebuie sa facem apelarea ei.
#                 # Instructiunile dintr-o functie se vor executa DOAR DACA APELAM FUNCTIA.
#                 # Apelarea se face prin scrierea numelui functiei urmat de doua paranteze
#                 # rotunde in interiorul carora vom pune (daca este cazul) unul sau mai
#                 # multe argumente.
#
# """
# Exista patru tipuri de functii in Python:
# 1. Functii simple.
# 2. Functii cu parametri.
# 3. Functii cu return.
# 4. Functii cu parametri si return.
#
# PARAMETRII: un parametru este o adresa de memorie temporara care se populeaza atunci cand functia este
# apelata. Parametri sunt reprezentati de un nume care este specificat intre parantezele rotunde la
# apelarea functiei si care au rolul de a stoca informatii venite din exterior. Aceste informatii vor
# fi utilizate in momentul executarii instructiunilor.
#
# Parametri sunt de doua feluri:
# -- parametri expliciti = sunt acei parametri specificati in mod direct in definitia functiei
# -- parametri impliciti = in cazul in care nu vor primi valoare la apelarea functiei se vor folosi
#                            implicit valoarea specificata la definirea functiei.
# """
#
#
# # Exemplu de parametri expliciti
# def salutare_cineva(nume):          # 'nume' este parametru explicit
#     print(f"Salut, {nume}!")
#
# salutare_cineva('Valentin')         # la apelare numele valorilor efective care sunt transmise
#                                     # functiilor se numesc argumente. Deci 'Valentin' este un argument.
#
#
#
# # Exemplu de parametri impliciti
# def salutare_cineva(nume='Ioana'):  # aceasta functie are un singur parametru explicit, care are
#                                     # o valoarea implicita.
#     print(f"Salut, {nume}!")
# salutare_cineva()                   # la apelarea acestei functii nu am furnizat un argument
# salutare_cineva('Cristi')           # la aceasta apelare am furnizat si argument, iar in acest caz
#                                     # valoarea implicita (Ioana) setata la definirea functiei va fi
#                                     # ignorata deoarece am furnizat un argument explicit
#
# """
# RETURN
# este modalitatea prin care putem sa transmitem rezultatul functiei in exterior (adica sa o vizualizam)
# De exemplu, daca vrem sa calculam suma a doua numere si sa o afisam pe ecran in momentul apelarii functiei
# va trebui sa aveam instructiune de return, altfel adunarea se va executa dar noi nu vom putea valida acest
# lucru deoarece nu va fi afisat nicaieri.
# """
#
# # Exemplu de functie cu return
#
# def adunare(a, b):
#     rezultat = a + b    # se realizeaza adunarea parametrilor a si b,
#                         # iar rezultatul este stocat in variabila rezultat
#     return rezultat     # aceasta este valoarea pe care o va primi orice cod care apeleaza aceasta functie
#
# suma = adunare(3,8)
# print(f"Suma este: {suma}")
#
# # functii cu numar indefinit de parametri
# # in Python poti defini functii care sa accepte un numar variabil de parametri.
# # pentru asta ne folosim de functia Python numita "*args" si "**kwargs"
#
# # exemplu de functie cu *args
#
# def functie_variabila(*args):   # functia a fost definita cu un singur parametru '*args', aratand ca functia accepta un numar variabil de argumente
#     rezultat = 0                # se initializeaza variabila la 0, pentru a fi utilizata  pentru a stoca suma argumentelor
#     for numar in args:          # bucla 'for' itereaza prin toate argumentele furnizate si adauga fiecare la variabila 'rezultat'.
#         rezultat += numar
#     return rezultat
#
# rezultat1 = functie_variabila(1, 2, 3)      # se apeleaza functia cu 3 argumente, iar rezultatul va fi stocat in aceasta variabila (rezultat)
# rezultat2 = functie_variabila(4,5,6,7,8,9,10)
# print(f"rezultat1 : {rezultat1}")
# print(f"rezultat2 : {rezultat2}")
#
#
# # Functii cu **kwarg
#
# def informatii_studenti(**kwargs):         # foloseste parametrul  ***kwargs aratand ca functia accepta un numar variabil de argumente keyword
#     for cheie, valoare in kwargs.items():  # utilizam bucla "for" pentru a itera prin perechile cheie-valoare din kwargs
#         print(f"{cheie} {valoare}")        # fiecare pereche cheie-valoare va fi afisata in consola
#
# informatii_studenti(nume = "John", varsta = 20)   # se apeleaza functia furnizand argumente de tip cheie-valoare (nume = John)
# informatii_studenti(nume = "Alice", varsta = 25, nota = 10, cursul = 'Biologie')
#
#
# # Exercitiu: sa calculam aria unui cerc.
#
# def aria_cerc(raza):
#     return math.pi * raza ** 2
# rez = aria_cerc(3)
# print(f"{rez}")
#
#
#
# # =====================================================================
#
# # Exceptii
# # TRATAREA EXCEPTIILOR
#
# """
# Este o tehnica de gestiunare a situatiilor exceptionale care pot aparea in timpul executiei
# unei bucati de cod sau a codului intreg.
# Exceptiile sunt evenimente neasteptate care pot provoca intreruperea rularii codului.
# Sunt utile atunci cand nu ne dorim oprirea codului.
# Structura tratarii exceptiilor:
#     try = inceputul blocului de exceptie;
#     caracterul ":" = marcheaza inceputul blocului de cod care se incearca a se executa;
#     except = este inceputul blocului de tratare exceptii
#     caracterul ":" = care marcheaza inceputul blocului de cod de tratare a exceptiilor;
#     blocul de cod care se executa atunci cand se produce o exceptie.
#
# """
#
# # Exemplu:
# # print(10/0)
#
# try:
#     print(10/0)
# except:
#     print("Impartirea la zero nu este permisa.")
#
#
# try:
#     rezultat = 10/0
# except ZeroDivisionError:    # este denumirea erorii care apare in caz ca vrem sa impartim 10 la zero.
#     print("Eroare : impartirea la 0 nu este permisa.")  # Blocul de cod se executa daca aparea exceptia specifica.
#
# def impartire(a, b):
#     try:
#         rezultat3 = a / b
#         print(f"rezultatul impartirii: {rezultat3}")
#     except ZeroDivisionError:
#         print("Nu se poate efectua impartirea.")
#
# impartire(9,3)
#
#
# # Exceptii = poti ridica o exceptie manual, folosind instructiunea "raise" (ridicare unei exceptii).
# # Ridicarea manuala a unei exceptii este utila atunci cand vrei sa semnalezi ceva anormal in program
# # si sa fortezi o executie alternativa.
#
#
# # Exemplu de exceptie.
#
# nota_elev = int(input("Va rugam sa introduceti nota care trebuie sa fie procesata: "))
# if nota_elev < 5:     # verificam conditia daca nota elevului este mai mica decat 5.
#     raise Exception("Nota cursantului este prea mica.")    # daca conditia de mai sus este indeplinita
#                                 # atunci este executata instructiunea de raise.

# Prin folosirea raise programul semnaleaza explicit ca se afla intr-o situatie exceptionala, unde
# nota studentului este considerata ca fiind prea mica.
# Functia raise este utilizata in general doar de programatori.from


# DEBUGGING =  reprezinta procesul de analiza a codului prin care putem sa observam cum circula datele
#              prin intermediul caruia putem sa identificam potentialele probleme.
# Pentru a putea face debugging trebuie sa punem un break point in locul unde vrem sa vedem cum
# circula datele. Se pot pune multiple break point-uri.
# Un break-point este un loc unde codul se opreste inainte sa execute urmatoarea instructiune.

# Ca sa punem un break-point dam click pe marginea din stanga a fisierului intre cifre si marginea fisierului.
# Dupa ce am pus break-point-ul de care avem nevoie dam click dreapta si "Debug"


lista_masini = ["Audi", "Skoda", "Ferari", "Dacia", "Mercedes", "Tesla", "Toyota", "Volkswagen"]
i = 0
while i < len(lista_masini):
    if lista_masini[i] == "Mercedes":
        print("Am gasit masina dorita de Dvs.")
        break
    i += 1
