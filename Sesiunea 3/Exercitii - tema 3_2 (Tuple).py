# --------------------------------------------------------------------------------
#1. Declarati un tuplu.

tupla1 = (4, 7, "Alin", 8.12, True, 55.33)
print(f"Tupla mea este: {tupla1}")

# --------------------------------------------------------------------------------
#2. Declarati un tuplu gol.

tupla2 = ()
print(f"Tupla mea goala arata asa: {tupla2}")



# --------------------------------------------------------------------------------
#3. Accesati orice element din tuplu pe baza de index.

tupla3 = (4, 7, "Alin", 8.12, True, 55.33, 6, 6, 21)
lungime_tupla = len(tupla3)
print(f"Tupla mea este: {tupla3}")
print(f"Primul element din tupla este:  {tupla3[0]}")
print(f"Al treilea element din tupla este:  {tupla3[2]}")
print(f"Ultimul element din tupla este:  {tupla3[lungime_tupla-1]}")



# --------------------------------------------------------------------------------
#4. Accesati pozitia unui element din lista pe baza functiei index().

print(f"Elementul 'Alin' este la pozitia {tupla3.index('Alin')} in tupla.")


# --------------------------------------------------------------------------------
#5. Folositi functia count() pentru a numara de cate ori apare un element in tuplu.

print(f"Elementul '6' apare de {tupla3.count(6)} ori in tupla.")


# --------------------------------------------------------------------------------
#6. Folositi functia index() pentru a verifica pozitia la care se afla un
#   anumit element in tuplu.

tupla3 = (4, 7, 'Alin', 8.12, True, 55.33,6, 6)
element_cautat = 'Alin'
pozitie_indicata = 3
pozitie_gasita = tupla3.index(element_cautat)
if (pozitie_gasita == pozitie_indicata-1):
    print(f"Tupla mea este: {tupla3}")
    print(f"Elementul {element_cautat} este intr-adevar la pozitia {pozitie_indicata} in tupla.")


# --------------------------------------------------------------------------------
#7. Incercati sa modificati un element din tuplu si observati rezultatele.

# NU se pot modifica elementele dintr-o tupla.