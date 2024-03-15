# --------------------------------------------------------------------------------
#1. Declarati un set.

set1 = {1, 3, 5, 4, 78, 90, 12, 33}
print(f"Setul meu este: {set1}")


# --------------------------------------------------------------------------------
#2. Declarati un set gol.

set2 = {}
print(f"Un set gol arata asa: {set2}")

# --------------------------------------------------------------------------------
#3. Adaugati un element nou in set folosind functia add().

set3 = {1, 3, 5, 4, 78, 90, 12, 33}
print(f"Setul meu este: {set3}")
element = 77
print(f"Voi adauga elementul: {element}")
set3.add(element)
print(f"Acum, setul meu arata asa: {set3}")



# --------------------------------------------------------------------------------
#4. Stergeti un element din set folosind functia pop()
#   si respectiv functia remove(). Observati rezultatele.

set4 = {1, 3, 5, 4, 78, 26, 90, 12, 33}
print(f"Setul meu este: {set4}")
set4.pop()   # sterge primul element din set
print(f"Setul sters cu pop este: {set4}")

set4.remove(5)  # sterge elementul cu valoarea specificata ('5').
print(f"Setul sters cu remove: {set4}")



# --------------------------------------------------------------------------------
#5. Verificati daca un set este o subdiviziune a unui alt set (subset).

set5 = {26, 12, 3}
print(set5.issubset(set4))


# --------------------------------------------------------------------------------
#6. Verificati daca un set contine toate elementele
#   dintr-un alt set + alte elemente (superset).

set6 = {26, 12, 3}
print(set6.issuperset(set4))

# --------------------------------------------------------------------------------
#7. Verificati care sunt elementele comune intre doua seturi (intersection).

set7 = {2, 3, 26, 100, 81}
intersectia = set4.intersection(set7)
print(f"Intersectia celor 2 seturi: {diferenta}")



# --------------------------------------------------------------------------------
#8. Verificati diferenta intre doua seturi cu functia difference().

set7 = {2, 3, 26, 100, 81}
diferenta = set4.difference(set7)
print(f"Difereta celor 2 seturi: {diferenta}")
                # elementele pe care le are in plus set4 fatza de set7


# --------------------------------------------------------------------------------
#9. Stergeti toate elementele dintr-un set folosind functia clear().

set_sters = set7.clear()
print(f"Setul sters este {set_sters}")