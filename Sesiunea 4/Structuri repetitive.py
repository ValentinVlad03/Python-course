# STRUCTURI REPETITIVE
# structurile repetitive sunt :  while, for, for each (cele mai utilizate sunt while si for)
# Structurile repetitive sunt utilizate pentru a executa aceeasi secventa de instructiuni de mai multe ori
# pana cand o anumita conditie nu mai este indeplinita


# structura WHILE
# executa o secventa de instructiuni atata timp cat este adevarata.
# Se foloseste atunci cand nu stim exact momentul in care conditia nu mai este adevarata.
# Componentele unui WHILE:
#      a)  o variabila de control al while-ului (desi nu este obligatoriu)
#      b)  inceputul while-ului marcat prin cuvantul WHILE
#      c)  conditia de evaluare (cea pe baza careia se decide daca se mai trece o data prin while sau nu)
#      d)  separatorul intre conditia de evaluare si corpul while-lui ":"
#      e)  corpul while-ului (adica o serie de instructiuni care se vor repeta)


# Exemplul 1
suma = 0
i = 1   # aceasta este o variabila de iteratie

while i >= 1 and i <= 10 :
    suma = suma + i
    print(f"Am adunat numarul {i}")
    i += 1
print(f" Suma: {suma}")


# Exemplul 2
numar = 1
while numar <= 5 :
    print(numar)
    numar += 1

# Exemplul 3:  vreau sa printez 101 dalmatieni

numar_dalmatieni = 1
while numar_dalmatieni <= 101 :
    print(f"Catelusul dalmatian de acum are numarul {numar_dalmatieni}")
    numar_dalmatieni += 1


# ----------------------------------------------
# FOR
# este o structura repetitiva care executa un set de instructiuni pe baza unui range si care se
# foloseste atunci cand stim exact de cate ori vrem sa parcurgem un anumit set de instructiuni.
# Se bazeaza pe o variabila de iteratie care va stoca rand pe rand valoarea din range

# Componentele unui ciclu FOR
#     a) inceputul FOR-ului marcat prin cuvantul "FOR"
#     b) variabila de iteratie care va stoca indexul din range
#     c) range-ul sau structura repetitiva care este parcursa
#     d) separatorul de range ":"
#     e) corpul FOR-ului (adica setul de instructiuni)


# Exemplu: vreau sa calculez suma numerelor de la 1 la 10

suma = 0
for i in range(1,11):
    suma += i
print(f"Valoarea curenta a sumei este: {suma}")


# Exemplu: Iterare printr-o lista
fructe = ["mar", "banana", "cirese"]
for fruct in fructe:
    print(fruct)

# Exemplu:  cei 101 dalmatieni
numar_dalmatieni = 1
for i in range (1,102):
    print(f"Dalmatianul curent are numarul {i}")



# ----------------------------------------------
# FOR EACH
# diferenta intre FOR si FOR EACH este aceea ca in cazul FOR-ului variabila de iteratie
# stocheaza indexul curent al elementului din lista in timp ce la FOR EACH variabila de iteratie
# stocheaza valoarea curenta a elementului aflat la un anumit index.

# Exemplul 1
lista = [1, 2, 3, 4]
for element in lista:
    print(element)

# in concluzie FOR este mai util atunci cand vrem sa modificam o valoare in lista
# pentru ca se acceseaza pe baza de index.
# FOR EACH este mai util atunci cand vrem sa scoatem un element din lista pentru a nu se calcula
# lungimea listei.


# ----------------------------------------------
# Metode de control al structurilor repetitive

# Exista cateva metode de control al structurilor repetitive (bucle), cum ar fi "break",
# "continue" si "else" in buclele "for" si "while".

#  a) BREAK - incheie executia tuturor iteratiilor curente si viitoare in bucla

# Exemplu:
for i in range(1,11):
    if i == 5:
        break
    print(i)


#  b) CONTINUE - sare peste iteratia curenta dar executa iteratia viitoare

# Exemplu:
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#  c) ELSE in bucla FOR = este executata atunci bucla se termina normal (fara a fi intrerupta de break)

# Exemplu:

for i in range(1,6):
    print(i)
else:
    print("Bucla a fost parcursa complet.")


#  d) ELSE in bucla WHILE = este executata atunci cand conditia din bucla devine falsa.

# Exemplu:
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Conditia nu mai este adevarata.")


# exemplu: vrem sa parcurgem o lista de masini si sa alegem din lista doar daca masina este Mercedes

lista_masini = ["Audi", "Skoda", "Ferari", "Dacia", "Mercedes", "Tesla", "Toyota", "Volkswagen"]
i = 0
while i < len(lista_masini):
    if lista_masini[i] == "Mercedes":
        print("Am gasit masina dorita de Dvs.")
        break
    i += 1
