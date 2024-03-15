# STRUCTURI DE DATE
# Structurile de date reprezinta adrese de memorie care pot stoca mai multe valori.
# Exista patru tipuri de structuri de date: Liste, Seturi, Tupluri si Dictionare

# Listele = structuri de date care permit stocarea si manipularea unui numar variabil de elemente
# - sunt definite prin incadrarea elementelor intre paranteze drepte
# - listele sunt ordonate si indexate (indexarea incepe de la zero), sunt mutabile (adica pot fi modificate)
# se pot adauga, sterge si modifica elementele din lista dupa ce au fost create.
# Listele sunt definite prin incadrarea elementelor intre paranteze drepte.
# Lista permite elemente duplicate.
# Adaugarea elementelor se poate face la finalul listei cu functia APPEND dar se poate face adaugare si in interiorul
# listei cu functia INSERT(). Stergerea elementelor din lista se face atat prin metoda POP cat si prin functia DEL.
# Prin metoda POP se sterge ultimul element din lista.
# Prin functia DEL se sterge un element de la un anumit index precizat.

lista = [1, 2, 3, "patru", 5.1, True]
print(f"Aceasta este lista mea: {lista}.")
print(f"Tipul listei este {type(lista)}")


#indexarea listelor
primul_element = lista[0]
print(primul_element)

al_doilea_element = lista[1]
print(al_doilea_element)

print(f"Acesta este elementul de la index 3: {lista[3]}")   # <<< este metoda recomandata pentru a face economie de cod


# slicing pe o lista - permite extragerea unei portiuni din lista
print(f"Portiunea din lista este {lista[1:3]}")
print(f"Portiunea din lista este {lista[3:5]}")
print(f"Portiunea din lista este {lista[:5]}")


# Adaugarea de elemente intr-o lista
lista.append(3)
print(f"Am adaugat un nou element si lista arata asa: {lista}")
lista.insert(1,9)
print(f"Am adaugat un nou element si lista arata asa: {lista}")


# Stergere de elemente din lista
# --- cu metoda POP
print(f'Am sters un element prin metoda pop cu argument, elementul sters este {lista.pop(1)}')
print(f"Lista mea arata asa: {lista}")
lista.append(10)
print(lista)
print(f'Am sters un element prin metoda pop fara sa dau argument, elementul sters este {lista.pop()}')

del lista[3]    # sterge elementul cu index 3 din lista mea.
print(f"Asa arata lista dupa ce am folosit functia DEL : {lista}")

lista.remove(5.1)  # specificam efectiv ce element vrem sa stearga
print(f"Asa arata lista dupa ce am folosit functia REMOVE : {lista}")


# Concatenare de doua liste - se foloseste operatorul +

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concetenata = lista1 + lista2
print(f"Lista concatenata este : {lista_concetenata}")


# Extindere de lista folosind metoda extend()

lista1.extend(lista2)
print(f'Am extins lista1 cu elementele din lista2. Lista1 arata acum asa: {lista1}')

print(f'Am folosit functia len, lista are lungimea de {len(lista)} elemente.')
print(f'De cate ori apare cifra 3 in lista? De {lista.count(3)} ori.')
print(lista)


# sortarea ascendenta a elementelor din lista
print(f'Lista sortata este urmatoarea: {sorted(lista)}')

# # sortarea descendenta a elementelor din lista
# lista.sort(reverse = True)
# print(f'Lista sortata descendent este urmatoarea: {lista}')

print(f'Indexul primei cifre 3 gasita in lista este: {lista.index(3)}')
print(f'Indexul primei cifre 2 gasita in lista este: {lista.index(2)}')

# ----------------------

lista6 = [1, 2, 3, 5.1, 9, -1]
print(f'Cifra cea mai mare din lista este {max(lista6)}')
print(f'Cifra cea mai mica din lista este {min(lista6)}')



# ------------------------------------------------------------------------

# SETURILE
# sunt colectii de date neordonate (neindexate), nu permit elemente duplicate (deci au doar elemente unice),
# Seturile nu au o ordine definita. Faptul ca nu sunt ordonate nu ne permite sa accesam elemente pe baza de index.
# Nu putem adauga un element la o anumita pozitie si nu ne lasa sa extragem un singur element din set.
# Aceasta poate fi gestionata doar in intregime.
# Seturile sunt definite de paranteze ondulate (acolade) {}
# Orice element care este duplicat va fi ignorant. (Nu va returna eroare, dar nici nu va adauga elementul.)

set1 = {1, "sapte", 2, 9, 3.23, True}
print(set1)


# Existenta unui element in set
exista = 3 in set1
print(exista)
print(f'Exista elementul 3 in set ?  {3 in set1}')


# adaugare element in set
set1.add(47)
print(f'Setul meu dupa adaugarea unui element nou arata asa: {set1}')


# stergerea unui element
set1.remove(47)
print(f'Setul meu dupa stergerea unui element (47) arata asa: {set1}')


# Unirea de seturi
set2 = {1, 2, 3}
set3 = {3, 4, 5}
seturi_unite = set2.union(set3)
print(f"Noul set format va fi asa: {seturi_unite}")


# Intersectia seturilor
intersectie = set2.intersection(set3)
print(f'Intersectia celor doua seturi este: {intersectie}')


# Diferenta seturilor
diferenta = set2.difference(set3)
print(f'Diferenta celor doua seturi este: {diferenta}')