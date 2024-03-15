# # - cu diez punem comentarii pe o singura linie
# """
# intre aceste ghilimele se pot pune comentarii pe mai multe linii iar editorul de cod le va ignora.
#
# variabila = 20     # am declarat o variabila
#
# """
# # linia aceasta vreau sa fie comentata
#
# # - cu combinatia tastelor CTRL + ?  putem comenta o linie selectată
#
# # VARIABILA - sunt adrese de memorie care stochează diverse valori
# # valori care se pot modifica pe parcursul execuţiei codului.
#
# numar_intreg = 15
# print(numar_intreg)
#
# # CamelCase - consta in a incepe un cuvant cu o litera mare, fara
# # sa folosim spatii sau caractere cu subliniere intre cuvinte
# NumeVariabila = 15
#
# # SnakeCase - consta in folosirea de litere mici si adaugarea de
# # caractere de subliniere intre cuvinte
# nume_variabila = 15
#
# # cele 2 variabile de mai jos sunt considerate ca fiind diferite, distincte din cauza modului de scriere a lor:
# # myvar = 15
# # myVar = 15
#
# numar_intreg = 15   # (int)
# numar_cu_virgula = 3.14   # (float)
# text = "Salut! Buna seara!"   # (string)
# lista = [1,2,3,4]    # (lista)
#
#
# # TIPURI DE DATE - proprietati ale adreselor de memorie care definesc ce fel de informatii pot fi stocate
# # la acea adresa de memorie.
# # Tipul de date poate varia in functie de valoarea salvata la acea adresa de memorie.
# # Tipuri de date cele mai cunoscute:
# # - numeric :  int (integer)   --- myvar = 42
# # - float :  numere cu virgula    --- myvar = 3.14
# # - sir de caractere :  str (string)   --- myvar = "Buna ziua!"
# # - valori logice :   bool (boolean)  ----   myvar = True
# # - structuri de date secventiale:    list (lista) = [1,2,3]
# #                                     tupla = (1,2,3)
# # - structuri de date mapping :    dict (dictionar) = {cheie : valoare}
# # - structuri de date de tip set :    set (seturi) = {1,2,3,4}
#
# ani = 5   # am initializat o variabila cu valoarea 5, reprezentata de tipul de date int
# ani1 = "cinci"     # am initializat o variabila cu valoarea "cinci" de tipul de date string
#
# # PRINT - o functie care ne ajuta sa afisam informatii in consola
# print(text)
# print(lista)
#
# # Tiparirea cu formatare este modalitatea prin care putem integra o variabila in interiorul unui string
# # Pentru tipurile de date de tip string semnul plus este folosit pentru a concatena doua siruri de caractere.
#
# # print("Ana are " + 12 + "ani")   --- aici am incercat sa concatenam date de tip string cu int si am primit eroare
# # print("Ana are " + str(12) + " ani.")   --- aici am folosit type casting
#      # adica am fortat ca numarul 12 sa fie de tip string,
#      # nu am primit eroare dar codul este incarcat si greu de citit.
#
# print(f"Ana are {12} ani")
#
# varsta = 12
# print(f"Ana are {varsta} ani.")
#
# # CONSTANTELE - este o adresa de memorie care stocheaza o valoare.
# # de obicei constantele sunt denumite cu litere majuscule si cu sublinierea intre cuvinte
# PI = 3.14159
# MAX = 100
# print(PI)
# varsta = 15
# print(f"Ana are {varsta} ani.")
#
# # Functia TYPE ()
# # Functia Type este o logica de cod prodefinita ce are rolul de a face conversia ...
# # Functia Type este o functie care returneaza tipul de date al unei variabile si nu numai
#
# # x = 5
# # print(type((x))
# # y = "Hello"
# # print(type((y))
# # z = [1,3,9]
# # print(type((z))
#
# # TYPE CASTING - transforma o valoare dintr-un tip de date in altul
# # type castingul este adesea necesar cand se lucreaza cu diferite tipuri de date
# # sau atunci cand se doreste sa ne asiguram ca o valoare este un anumit tip de date
# # Castingul trebuie sa fie compatibil. Nu se poate face conversie din string in int
# # pentru ca va returna eroare
#
# # Mai jos incercam sa facem type casting dintr-o valoare de tip string in tip int
#
# # nume = "cinci"
# # int_nume = int(nume)
# # print(int_nume)
#
# # Mai jos incercam sa facem type casting dintr-o valoare boolean in int.
# # Va fi transformat True in 1 iar False in 0.
#
# x = True
# y = int(x)
# print(f"Am fortat variabila sa fie in {y}.")
#
# d = 4.58976
# f = int(d)
# print(f"Valoarea fara zecimale este {f}.")
#
# nume1 = "Ioana"
# an = 1990
# salariu = 9999.99
# angajat = True
#
# print(f"Ma numesc {nume1}, sunt nascuta in anul {an}, sunt angajata"
#       f"{angajat} si am salariul {salariu} lei.")
#
#
# numele_meu = "Cristina"
# print("Numele meu este: ", numele_meu)
#
# nume10 = "Ana"
# ani = 25
# print("Nume:", nume10, ", in varsta de", ani, "ani.")


# Functia INPUT
# Functia input este folosita pentru a citi o linie de intrare de la un utilizator / tastatura.
# Functia input returneaza o valoare citita sub forma de sir de caractere
# si o folosim pentru a interactiona cu utilizatorul, pentru a obtine date de intrare in timpul executarii codului.

# nume_utilizator = input("Va rugam introduceti numele Dvs.: ")
# print(f"Salut, {nume_utilizator}!")

prenume = input("Va rugam sa va introduceti prenumele Dvs. : \n")
nume = input("Va rugam sa va introduceti numele Dvs.: \n")
print(f"Buna! Numele tau complet este: {prenume} {nume}!")


