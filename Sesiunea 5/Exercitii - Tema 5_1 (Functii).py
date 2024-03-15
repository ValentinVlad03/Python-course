# --------------------------------------------------------------------------------
# 1. Definiti o funcție fara parametri si fara return care să calculeze și să
#    returneze suma a două numere.

def suma_a_doua_numere():
    x = int(input("x: "))
    y = int(input("y: "))
    suma = x + y
    print(f"x + y = {suma}")

suma_a_doua_numere()




# --------------------------------------------------------------------------------
# 2. Definiti o funcție care să returneze TRUE dacă un număr este par sau FALSE
#    daca numarul este impar

def par_impar(a):
    if a % 2 == 0:
        nr_par = True
    else:
        nr_par = False
    return nr_par

x = int(input("Numar: "))
if par_impar(x):
    print(f"Numarul {x} este par.")
else:
    print(f"Numarul {x} este impar.")


# --------------------------------------------------------------------------------
# 3. Definiti o funcție o care returnează numărul total de caractere din
#    numele tău complet (nume, prenume, nume_mijlociu)

# Varianta 1 de solutie
def nr_caractere(text):
    cuvinte = nume.split()  # Nu tine cont de faptul ca numele poate fi din 2 cuvinte separate de "-"
                            # De exemplu:  Rodica Popescu-Bitanescu
                            # Aici va numerota si cratima dintre cele doua cuvinte de la nume.
    nr_cuvinte = len(text_fara_spatii)
    lungime = 0
    for i in range (0, nr_cuvinte):
        lungime += len(text_fara_spatii[i])
    return lungime

nume = str(input("Numele tau complet: "))
x = nr_caractere(nume)
print(f"Numele tau are {x} caractere.")


# Varianta 2 de solutie (mai buna!)
def nr_caractere(text):
    lungime_text_initial = len(text)
    total_litere = 0
    separatori = [' ', '-', '.']    # Aici am definit separatorii posibili ce pot fi introdusi de user
    for i in range(0,lungime_text_initial):
        char = text[i]
        if not (char in separatori):
                total_litere += 1
    return total_litere

nume = str(input("Numele tau complet: "))
x = nr_caractere(nume)
print(f"Numele tau are {x} caractere.")



# --------------------------------------------------------------------------------
# 4. Definiti o funcție care returnează aria unui dreptunghi cu
#    laturile primite prin parametru.
def aria_dreptunghi(lungime, latime):
    aria = float(lungime) * float(latime)
    return aria

x = float(input("Lungimea : "))
y = float(input("Latimea : "))
aria = aria_dreptunghi(x, y)
print(f"Aria dreptunghiului: {aria}")



# --------------------------------------------------------------------------------
# 5. Definiti o funcție care calculeaza aria unui cerc si o returneaza.
#    Raza va fi primita prin parametru.

import math

def aria_cercului(raza):
    aria = math.pi * (raza ** 2)
    return aria

r = float(input("Raza cercului: "))
aria_afisata = round(aria_cercului(r), 2)  # am rotunjit ca să afişeze doar primele 2 cifre după vorgulă
print(f"Aria cercului: {aria_afisata}")



# --------------------------------------------------------------------------------
# 6. Funcție care returnează TRUE dacă un caracter x se găsește
#    într-un string dat și FALSE in caz contrar.

def gaseste_caracter(text, caracter):
    lungime_text = len(text)
    am_gasit = False
    for i in range(0,lungime_text):
        if caracter == text[i]:
            am_gasit = True
            break
    return am_gasit

textul = str(input("Introduceti textul: "))
caracter_cautat = str(input("Introduceti caracterul de cautat: "))
if gaseste_caracter(textul, caracter_cautat):
    print (f"Caracterul '{caracter_cautat}' apare in textul de mai sus.")
else:
    print(f"Caracterul '{caracter_cautat}' nu apare in textul de mai sus.")



# --------------------------------------------------------------------------------
# 7. Definiti o funcție fără return care primește un string și printează pe ecran:
#         -- Numărul de caractere lower case este x
#         -- Numărul de caractere upper case exte y

def tip_caractere_in_text(text):
    lungime_text = len(text)
    caractere_lower_case = 0
    caractere_upper_case = 0
    for i in range(0,lungime_text):
        if text[i].islower():
            caractere_lower_case += 1
        if text[i].isupper():
            caractere_upper_case += 1
    print(f"Numărul de caractere lower case este: {caractere_lower_case}")
    print(f"Numărul de caractere upper case este: {caractere_upper_case}")

textul_de_analizat = str(input("Textul este: "))
tip_caractere_in_text(textul_de_analizat)



# --------------------------------------------------------------------------------
# 8. Definiti o funcție care primește ca parametru o LISTĂ de numere
#    și returnează o alta LISTĂ doar cu numerele pozitive

def creare_lista_nr_pozitive(lista_originala):
    nr_elemente = len(lista_originala)
    lista_elem_pozitive = []
    for i in range(0, nr_elemente):
        if lista_originala[i] > 0:
            lista_elem_pozitive.append(lista_originala[i])
    return lista_elem_pozitive

lista1 = [1, 56, -23, -45, 3, 91, 10]
print(f"Lista initiala: {lista1}")
lista_finala = creare_lista_nr_pozitive(lista1)
print(f"Lista rezultata: {lista_finala}")



# --------------------------------------------------------------------------------
# 9. Definiti o funcție care nu returneaza nimic dar care primește
#    două numere și PRINTEAZĂ:
#        -- Primul număr x este mai mare decat al doilea număr y
#        -- Al doilea număr y este mai mare decat primul număr x
#        -- Numerele sunt egale.

def nr_comparate(x, y):
    if x > y:
        print(f"Primul număr ({x}) este mai mare decat al doilea număr ({y}).")
    if y > x:
        print(f"Al doilea număr ({y}) este mai mare decat primul număr ({x}).")
    if x == y:
        print("Numerele sunt egale.")

a = float(input("x: "))
b = float(input("y: "))
nr_comparate(a, b)



# --------------------------------------------------------------------------------
# 10. Definiti o funcție care primește un număr și un set de numere.
#     Functia va face urmatoarele:
#         -- va printa ‘am adaugat numărul nou în set’ si va returna TRUE
#            daca numarul nu exista deja in set.
#         -- va printa ‘nu am adaugat numărul în set. Acesta există deja''
#                 si va returna FALSE daca numarul exista deja in set.

def verificare_numar_in_set(numar, lista):
    exista_deja = False
    if numar in lista:
        exista_deja = True
        print(f"Nu am adaugat numarul in set. El exista deja.")
    else:
        lista.append(numar)
        print(f"Am adaugat numarul nou ({numar}) in set.")
    return exista_deja


lista = [19, 5, 23, 22, 10, 8, 40]
print(f"Lista: {lista}")
nr = int(input("Nr.: "))
verificare_numar_in_set(nr, lista)



# --------------------------------------------------------------------------------
# 11. Definiti o funcție care primește o lună din an
#     și returnează câte zile are acea lună.

def zile_luna(luna):
    lista_zile = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    nr_zile = lista_zile[luna-1]
    return nr_zile

nr_luna = int(input("Luna nr.: "))
nume_luna = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie',
             'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie']
if nr_luna in range(1,12):
    print(f"Luna {nume_luna[nr_luna-1]} are {zile_luna(nr_luna)} de zile.")
else:
    print("Numar luna incorect.")



# --------------------------------------------------------------------------------
# 12. Definiti o funcție calculator care să returneze 4 valori: suma, diferența,
#     înmulțirea si împărțirea a două numere.

def calculator(a, b):
    suma = a + b
    diferenta = 0
    if a > b:
        diferenta = a - b
    else:
        diferenta = b - a
    produs = a * b
    impart = a / b
    return suma, diferenta, produs, impart

x = float(input("x = "))
y = float(input("y = "))
valori = calculator(x, y)
print(f"suma      = {valori[0]}")
print(f"diferenta = {valori[1]}")
print(f"inmultirea = {valori[2]}")
print(f"impartirea = {valori[3]}")



# --------------------------------------------------------------------------------
# 13. Definiti o funcție care primește o listă de cifre (adică doar 0-9)
#     si care returnează un dictionar care va contina cifra ca si cheie
#     si numarul de aparitii ale acelei cifre ca valoare

def calcul_aparitii(lista):
    nr_elemente = len(lista)
    dictionarul = dict()
    k = 0
    for i in range(0, nr_elemente):
        nr_aparitii = 1
        for j in range(0, nr_elemente):
            if (i != j) and (lista[i] == lista[j]):
                nr_aparitii += 1
        dictionarul[k]=(lista[i], nr_aparitii)
        k += 1
    return dictionarul

lista_cu_numere = [1, 5, 7, 3, 2, 1, 5, 9, 4, 4, 4, 5, 6]
print(f"Lista cu numere: {lista_cu_numere}")
print(f"Dictionarul arata asa: {calcul_aparitii(lista_cu_numere)}")


# --------------------------------------------------------------------------------
# 14. Definiti o funcție care primește 3 numere si returnează valoarea maximă dintre ele.

def maximul(a, b, c):
    max = 0
    if a > b:
        max = a
    else:
        max = b
    if max < c:
        max = c
    return max

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
print(f"Valoarea maxima este: {maximul(x, y, z)}")



# --------------------------------------------------------------------------------
# 15. Definiti o funcție care să primească un număr și să returneze suma
#     tuturor numerelor de la 0 la acel număr.

def suma_numerelor(numar):
    suma = 0
    for i in range(0,numar+1):
        suma = suma + i
    return suma

nr = int(input("numarul este: "))
rezultat = suma_numerelor(nr)
print(f"Suma numerelor pana la {nr} este: {rezultat}")



# --------------------------------------------------------------------------------
# 16. Definiti o funcție care sa primească 2 liste de numere (numerele pot fi dublate)
#     si sa returneze numerele comune.

def intersectie_liste(lista1, lista2):
    lista_nr_comune =[]
    # aici cream lista cu numerele comune
    for i in range(0, len(lista1)):
        for j in range(0, len(lista2)):
            if (lista1[i] == lista2[j]):
                lista_nr_comune.append(lista2[j])

    # aici eliminam dublurile, adica numerele care se repeta
    for i in range(0, len(lista_nr_comune)-1):
        for j in range(0, len(lista_nr_comune)-1):
            if (i != j) and (lista_nr_comune[i] == lista_nr_comune[j]):
                element = lista_nr_comune[j]
                lista_nr_comune.remove(element)

    return lista_nr_comune

lista_x = [1, 34, 23, 67, 67, 81, 40, 18]
lista_y = [2, 4, 23, 8, 10, 18, 67, 81]
print(f"Lista1 = {lista_x}")
print(f"Lista2 = {lista_y}")
print(f"Lista cu numerele comune este: {intersectie_liste(lista_x, lista_y)}")



# --------------------------------------------------------------------------------
# 17. Definiti o funcție care să aplice o reducere de preț.
#     Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
#     Tratează cazurile în care reducerea e invalidă.
#     De exemplu o reducere de 110% e invalidă.

def calcul_reducere(pret, reducere):
    if reducere in range(1, 100):
        pret_final = pret * (100 - reducere) / 100
    else:
        print("Reducerea este invalidă.")
    return pret_final

pret = int(input("Pret: "))
discount = int(input("Reducere: "))
pret_final = int(calcul_reducere(pret, discount))
print(f"Pretul final este: {pret_final} lei.")
