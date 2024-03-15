# TUPLE
# structuri de date asemanatoare cu listele, diferenta dintre liste si tuple este ca cele din urma
# sunt imutabile, ceea ce inseamna ca nu pot fi modificate dupa ce au fost create.
# Asta inseamna ca putem face orice operatie de accesare a elementelor dar nu putem folosi la ele
# operatii de adaugare, de stergere sau de modificare. Tuplele  sunt definite utilizand paranteze
# rotunde (), sau daca contin un singur element


# exemplu de tupla cu mai multe elemente
tupla1 = (1, 2, 3, "patru")
print(tupla1)

# exemplu de tupla cu un singur element
tupla2 = (5,)   # trebuie neaparat sa fie acea virgula dupa element
print(tupla2)
print(type(tupla2))



# Tupla fara paranteze (tupla packing)
tupla3 = 1, 2, 3
print(tupla3)
print(type(tupla3))


# tupla goala
tupla_goala = ()
print(tupla_goala)


# Indexarea tuplelor
primul_element = tupla1[0]
print(primul_element)
print(f"Primul element din tupla este: '{tupla1[0]}'")    # metoda recomandata ptr economisire de cod


# slicing tupla
print(f"Aceasta este o portiune din tupla: {tupla1[0:3]}")

# alterare tupla = se refera la procesul de parcurgere a elementelor dintr-o lista / tuipla / sir de caractere
# si prelucrarea fiecarui element intr-un mod specific. Irerarea este realizata cu ajutorul buclelor,
# de exemplu bucla "for".

for x in tupla1:
    print(x)   #  x va lua valoarea fiecarui element din tupla in timpul iterarii.

# Despachetare tuple (Tupla Unpacking) - este procesul de asignare a valorilor dintr-o tupla
# unor variabile individuale. Acest proces ajuta la lucrul cu tuplele in diferite contexte.
# Pentru a despacheta se poate face prin a folosi o tupla pe partea dreapta a unei instructiuni
# de atribuire si de a asigna valorile la variabile individuale pe partea stanga.

a,b,c,d = tupla1    # deci va fi asa:  a = 1,   b = 2,  c = 3, d = patru
print(f"Variabila 'd' are urmatoarea valoare: '{d}' ")
print(f"Variabila 'c' are urmatoarea valoare: '{c}' ")


# -----------------------------------------------------

# DICTIONARE

# Dictionarele sunt structuri de date flexibile si ordonate care asociaza chei unice cu valorile
# corespunzatoare. Dictionarele sunt mutabile, adica putem adauga, sterge sau modifica valori din
# interiorul unui dictionar. Cheile unui dictionar trebuie sa fie unice, dar valorile se pot repeta.
# Dictionarele sunt definite utilizand acolade "{}" si au un format   cheie:valoare.


# Dictionar  cheie:valoare
dictionar1 = {"cheie1": 10,
              "cheie2": "Cristina",
              "cheie3": 3.14}
print(dictionar1)
print(type(dictionar1))


# Dictionar gol
dictionar_gol = {}
print(dictionar_gol)


# Adaugarea unui element in dictionar
dictionar1["cheie4"] = "John"
print(dictionar1)

# Accesare valori prin cheie
print(f'Aceasta este valoarea cheii 2 din dictionar: {dictionar1["cheie2"]} ')

# Iterarea printr-un dictionar
for cheie, valoare in dictionar1.items():
    print(f"Cheia este: {cheie},  Valoarea este: {valoare}")

# apeland metoda items() asupra dictionarului se returneaza o secventa de tupluri de
# genul (("cheie1", 10), ("cheie2", "Cristina"), etc. etc.)

# Verificarea existentei unei chei
print(f"Exista 'cheia3' in dictionar ?  {'cheie5' in dictionar1} ")

# Stergem un element prin intermediul cheii
# del dictionar1["cheie1"]   # stergere prin metoda DEL
# print(dictionar1)
# dictionar1.pop("cheie4")
# print(dictionar1)          # stergere prin metoda POP


# Actualizarea valorilor unei chei
dictionar1["cheie2"] = "Valoarea_noua"   # actualizare folosind operatorul de atribuire
print(dictionar1)


dictionar1.update({"cheie3": "valoare_cu_update"})  # actualizare folosind metoda update
print(dictionar1)
# vezi ca daca nu dai corect numele cheii la actualizare, atunci o va considera ca fiind un element
# nou, deci va mai adauga un element la lista, la dictionar.

dictionar1.update({"cheia3": "valoare_cu_update"})
print(dictionar1)

# Dictionare imbricate (dictionar in dictionar), mai sunt cunoscute si ca dictionare embedded - nested

jucatori_de_fotbal = {
    "Ducadam":  {"varsta": 70, "numar_tricou": 10, "numar_meciuri": 50},
    "Nicolita": {"varsta": 45, "numar_tricou":7,
                 "titluri_campion":
                        {"balon_de_aur": 2016,
                        "jucatorul_anului": 2010,
                        "ani_castig": [2016, 2020, 2010]},
                  "numar_meciuri": 30}
                     }

print(f"Nicolita a fost jucatorul anului in:  "
      f"{jucatori_de_fotbal['Nicolita']['titluri_campion']['jucatorul_anului']}")
print(f"Al doilea an in care a castigat Nicolita a fost: "
      f"{jucatori_de_fotbal['Nicolita']['titluri_campion']['ani_castig'][1]}")

