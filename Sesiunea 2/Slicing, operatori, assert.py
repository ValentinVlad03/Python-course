# # String index = un sir de caractere este ordonat in sensul in care orice caracter din acel sir are
# # o pozitie specifica numita index.
# # in orice string indexul porneste de la pozitia 0.
# list = [1, 2, 3, 4, "Maria"]
#
# # elementul cu valoarea 1 are indexul 0.
# # elementul cu valoarea 2 are indexul 1.
# # elementul cu valoarea 3 are indexul 2, etc.
#
# element = list[2]   # accesarea elementului cu index 2, comanda va returna cifra 3.
# print(f"Elementul cu index 2 este: {element}")
#
# # indexarea negativa se foloseste pentru a accesa elemente in sens invers incepand de la -1 care reprezinta
# # ultimul element din sir,   -2 penultimul element, etc.
#
# last_element = list[-1]    # accesam ultimul element din lista, o sa returneze 4
# print(f"Ultimul element din lista este: {last_element}")
#
# # string length   - il folosim daca vrem sa aflam cate caractere are un string
# # ne folosim de functia length (len)
# my_text = "Hello, world!"
# lungime_text = len(my_text)
# print(f"Variabila mea", my_text, "are", lungime_text, "caractere.")
# print(f"Variabila mea are lungimea de {lungime_text} caractere.")
# print(f"Variabila mea are {len(my_text)} caractere.")   # prin metoda folosirii functiilor direct in print se face economie de cod.
#
# print(f"Lista mea are o lungime de {len(list)} caractere.")
# # vezi ca la extragerea lungimii din liste sau dictionare, functia LEN nu va numara virgulele si spatiile asa cum face la string-uri.
#
#
# # string slicing - o modalitate prin care putem sa extragem doar o parte, sau intreg, etc. dintr-un string.
# # Putem sa extragem atat intregul sir de caractere, cat si portiuni din el, de la o anumita pozitie pana la sfarsit
# # sau doar un sir de caractere din interior.
# # Structura unui slicing este  [pozitie_de_start:pozitie_de_end:steps]
# #   Atentie!!! Pozitia_de_end nu se ia in considerare ca si limita finala.
# # De exemplu, daca ne intereseaza sa extragem caracterele de la pozitia 3 la pozitia 8 (caracter cu caracter).
# # O sa scrien slicing-ul [3:9:1]
# # pozitia_de_start - pozitia de inceput a slicing-ului (in mod implicit se incepe de la index 0 (zero).
# # pozitia_de_end   - pozitia de final (nu e luat in considerare la calcul)
# # step  - pasul de parcurs (fiecare al catelea caracter este luat in considerare)
# # (simbolul doua puncte) ":" este separator de elemente.
# # in mod implicit pozitia de inceput este 0 (zero), pozitia de final este ultimul caracter, iar pasul este 1.
#
# str_exemplu = "Ana are mere"
# print(f'Primele 3 caractere din variabila noastra sunt: "{str_exemplu[0:3]}"')
# print(f'Ultimul caracter din variabila noastra este: "{str_exemplu[-1]}"')
# print(f'Ultimele 3 caractere din variabila sunt: "{str_exemplu[-3:]}"')
#                 # pentru a obtine ultimele 3 caractere ne folosim de '-3' ca sa incepem sa citeasca de la final ultimele 3 caractere
# print(f'Al 4-lea caracter de la final este: "{str_exemplu[-4]}"')
#
# poezie = ("Ana are mere si este fericita cu ele si vrea sa mearga acasa.")
# # Exercitiu:  extrageti toate caracterele de la inceput pana la sfarsit cu mentionarea pasului
# print(poezie[0:len(poezie):1])   # folosim functia len(poezie) pentru a determina lungimea sirului si apoi utilizam
#                                  # aceasta lungime pentru a accesa toate caracterele din sir si sa facem slicing
#
# # Exercitiu_2 :  extragem toate caracterele de la inceput pana la sfarsit
# folosind pozitia de inceput si sfarsit implicita
# print(poezie[::])   # va returna acelasi lucru ca mai sus doar ca nu specificam nici startul, nici end-ul, nici pasul
#
# # Exercitiu_3 :  extragem toate caracterele de la inceput pana la sfarsit dar sa imi afiseze caracterele din 2 in 2.
# print(poezie[::2])
#
# # Exercitiu :  extrage toate caracterele de la pozitia 5 la 10
# print(poezie[5:10])
#
# # Exercitiu :  extrage ultimele 3 caractere din string
# print(poezie[-3:])
#
# # Exercitiu :  printeaza stringul in ordine inversa
# print(poezie[::-1])
#
#
#
# # Metoda string = metoda care poate fi folosita pentru interactiunea cu stringurile
#
# print(poezie.lower())     # va transforma toate caracterele din string in litere mici
# print(poezie.upper())     # va transforma toate caracterele din string in litere majuscule
# print(poezie.count("e"))
# print(poezie.islower())   # returneaza un rezultat boolean (False), pentru ca string-ul incepe cu litera mare, deci nu are doar litere mici.
# print(poezie.rstrip())
#
# # Metoda split =  este folosit pentru a desparti un string intr-o lista de subsiruri
# # Sintaxa este   string_subsir = string.split(delimiter)
#     # string este stringul initial pe care dorim sa il impartim
#     # delimiter = este caracterul sau sirul de caractere pe baza caruia facam impartirea
#     # string_subsir = stringul care va rezulta
#     # in mod implicit se va face split dupa spatii (in cazul in care nu dam niciun argument functiei split)
#
# text = "Ana are pere si mere"
# print(f"Asa impartim sirul de caractere dupa spatii  {text.split()}")
# data = "22-11-2023"
# print(f'Asa facem split cu argument: {data.split("-")}')
#
# # Metoda Replace = este folosita pentru a inlocui toate caracterele unui subsir cu alt subsir de caractere
# # sintaxa_noua = string_initial.replace(subsir_vechi, subsir_nou, numar_inlocuiri)
# #       string_initial =  sirul initial de caractere in care o sa facem inlocuirea
# #       subsir_vechi = caracterele pe care dorim sa il inlocuim
# #       subsir_nou = caracterele cu care vom inlocui subsir_vechi
# #       numar_inlocuiri = (este optional si) specifica numarul maxim de inlocuiri.
#
# original = "Ana are mere. Ana este fericita."
# nou = original.replace("Ana", "Maria")
# print(original)
# print(nou)
#
#
# # Metodele isDecimal / isNumeric / isDigit =  au rezultat de tip boolean (True, False)
# #   a)  isDecimal = verificam daca toate caracterele sunt cifre zecimale (0-9)
#
# numar = "12432523"
# print(f"Este un numar zecimal?  '{numar.isdecimal()}'")
#
# #   b)  isnumeric = verifica daca toate caracterele din sir sunt caractere numerice, inclusiv
# cele care sunt cifre speciale
# numar1 = "2.5e10"
# print(f'Este de tip numeric? "{numar1.isnumeric()}"')
#
# #   c)  isdigit = verifica daca toate caracterele din sir sunt cifre (0-9) dar include si
# alte caractere numerice de tip binar, octal, etc.
# numar2 = "123456"
# print(f"Este de tip digit? {numar2.isdigit()}")
#
# # -----------------------------------
#
# # OPERATORII ARITMETICI
# # sunt utilizati pentru a efectua operatii matematice
# #    1) Operatorul de adunare
# a = 5+3      # variabila a va primi valoarea 8
# #    2) Operatorul de scadere
# b = 7-2      # variabila b va primi valoarea 5.
# #    3) Operatorul de inmultire
# c = 4*6      # variabila c va primi valoarea 24.
# #    4) Operatorul de impartire   - returneaza o valoare de tip float
# d = 10/3     # variabila d va primi valoarea 3,3333.
# #    5) Operatorul de impartire intreaga  '//' = efectueaza impartirea si returneaza partea intreaga a rezultatului
# e = 10//3    # variabila e va primi valoarea 3.
# #    6) Operatorul de rest '%' (modulo)
# f = 10%3     # variabila f va primi valoarea 1, deoarece restul impartirii lui 10 la 3 este 1.
# #    7) Operatorul de (ridicare la) putere  '**' = ridica un numar la putere
# g = 2**3     # variabila g va primi valoarea 8, deoarece 2 la puterea 3 este egal cu 8.
#
#
# #2. OPERATORII DE ATRIBUIRE
# # Operatori de atribuire = este utilizat pentru a atribui o valoare unei variabile.
# #    1) Operatorul de atribuire simplu '=' --- atribuie o valoare unei variabile/
# x = 5        # variabilei x i se atribuie valoarea 5.
# #    2) Operatorul de atribuire cu adaugare '+=' =  adauga o valoare la variabila existenta si actualizeaza variabila cu noul rezultat
# a = 10
# a += 5   # este echivalentul a = a + 5
# print(a)
# #    3) Operatorul de atribuire cu scadere  '-='  --- scade o valoare din variabila existenta si actualizeaza variabila cu noul rezultat
# b = 8
# b -= 3
# print(b)
# #    4) Operatorul de atribuire cu inmultire '*=' --- inmulteste variabila existenta cu o anumita valoarea si actualizeaza variabila cu noul rezultat
# c = 4
# c *= 2     # echivalent cu c = c*2
# print(c)
# #    5) Operatorul de atribuire cu impartire '/='   ---  imparte variabila existenta cu o anumita valoarea si actualizeaza variabila cu noul rezultat
# d = 20
# d /= 4       # echivalent cu  d = d/4
# d //=4    # vom avea rezultatul fara zecimale
# print(d)
# #    6) Operatorul de atribuire cu rest '%='   ---- calculeaza restul impartirii variabilei la o anumita valoare si actualizeaza variabila cu rezultatul
# e = 17
# e %= 5
# print(e)
#
#
# #3.  OPERATORII DE COMPARARE
# # sunt utilizati pentru a compara doua valori si a determina relatia dintre ele. Intotdeauna da rezultate de tip boolean.
# #    1) Operatorul egal  '=='   --- verifica daca doua valori sunt egale
# a = 5
# b = 7
# rezultat = (a==b)
# print(rezultat)
# #    2) Operatorul diferit  '!='    --- verifica daca valori sunt egale
# x = 10
# y = 10
# rezultat = (x!=y)
# print(rezultat)
# #    3) Operatorul mai mic '<'   --- verifica daca o valoare este mai mica decat alta
# p = 3
# q = 6
# rezultat = (p<q)
# print(rezultat)
# #    4) Operatorul mai mare '>'   --- verifica daca o valoare este mai mare decat alta
# #    5) Operatorul mai mic sau egal  '<='
# #    6) Operatorul mai mare sau egal  '>='
#
#
# #4.   OPERATORI LOGICI
# #       1) AND
# #       2) OR
# #       3) NOT
#
# #1. Operatorul AND returneaza True daca ambele expresii sau valori sunt adevarate
# numar = 10
# if numar >15  and  numar <=20:
#     print('Numarul este mai mare decat 15 si mai mic sau egal cu 20.')
# else:
#     print('Numarul nu satisface conditia.')
#
# x = 10
# rezultat_and = x>3 and x<13
# print(rezultat_and)
#
# #2. Operatorul OR returneaza True daca cel putin una din valori este adevarata.
# x = 1
# rezultat_or = x>3 or x<13
# print(rezultat_or)
#
# #3. Operatorul NOT - returneaza inversul valorii booleane a unei variabile.
# x = True
# rezultat_not = not x
# print(rezultat_not)
#
# # Prioritatea operatorilor logici este: NOT, AND, OR.
#
# #  ASSERT --- este folosit pentru a verifica daca o anumita conditie este adevarata.
# # Genereaza o exceptie de tip AssertionError in cazul in care conditia nu este adevarata.
# # Assert-ul este foarte des utilizat in testarea automata deoarece verifica daca conditiile
# # sunt indeplinite.
# # ASSERT-ul are urmatoarele componente:
# #           - pe prima pozitie >>> valoarea pe care o comparam
# #           - pe a doua pozitie >>>  valoarea cu care comparam, cele doua valori fiind separate de
# #           - de operatorul de comparare '=='
# #           Ultima pozitie e un mesaj (optional) care sa fie returnat in cazul in care cele doua valori sunt egale.
# #
# # x = 5
# # assert x>1, ("Valoarea lui x trebuie sa fie mai mare decat 1.")
# # print('x este mai mare decat 1')
# #
#
# # ----------------------------------
# # Structuri alternative:  IF, ELSE si ELIF
# # sunt utilizate pentru a crea ramificatii in cod in functie de conditii.
# # Aceste structuri sunt varianta automata a metodei de testare manuala Decision Coverage.
#
# x = 1
# if x>5 :
#     print("x este mai mare decat 5.")
# else:
#     print("x nu este mai mare decat 5.")
#
# # exemplu pentru ELIF
# nota = 50
# if nota>=90:
#     print("Nota este A.")
# elif 80 <= nota < 90:
#     print("Nota este B.")
# elif 70 <= nota < 80:
#     print("Nota este C.")
# else:
#     print("Nota este sub C.")
#
#
# # Exemplu de cod cu ELIF si ASSERT
# numar = int(input("Introduceti un nr.: \n"))
# if numar > 0 :
#     rezultat = "Numarul este pozitiv."
# elif numar < 0 :
#     rezultat = "Numarul este negativ."
# else:
#     rezultat = "Numarul este 0."
# assert rezultat == "Numarul este pozitiv." or rezultat == "Numarul este negativ." or rezultat == "Numarul este zero."
# print(rezultat)


# Exemplu de cod: daca un numar este par sau impar

numar1 = int(input("Introduceti numarul : \n"))
if (numar1%2) == 0 :
    print('Numarul este par.')
else:
    print('Numarul este impar.')