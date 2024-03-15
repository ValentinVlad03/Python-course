# --------------------------------------------------------------------------------
#1. Declarati o lista cu elemente multitype.

lista = [1, 45, 34.97, 10e6, 'tralala', False]
print(lista)


# --------------------------------------------------------------------------------
#2. Declarati o lista goala.

lista = []
print(lista)



# --------------------------------------------------------------------------------
#3. Accesati orice element din lista pe baza de index.

lista = [1, 45, 34.97, 10e6, 'tralala', False]
print(lista[1])      # Va returna '45', pentru ca al doilea element are index 1.


# --------------------------------------------------------------------------------
#4. Accesati pozitia unui element din lista pe baza functiei index().

lista = [1, 45, 34.97, 10e6, 'tralala', False]
print(lista.index(34.97))     # Va returna '2', pentru ca al treilea element are index 2.



# --------------------------------------------------------------------------------
#5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert().
#   Observati rezultatele.

lista = [1, 45, 34.97, 10e6, 'tralala', False]
print("----------------")
print(f"Lista initiala: \n"
      f"{lista}")
print("----------------")

element = lista.append(55)   # APPEND adauga elementul la finalul listei
print(f"Am introdus 55 la final: \n"
      f"{lista}")
print("----------------")

element = lista.insert(2, 88)   # prin INSERT adaugam elementul la pozitia dorita
print(f"Am introdus 88 ca fiind al 3-lea element: \n"
      f"{lista}")
print("----------------")



# --------------------------------------------------------------------------------
#6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove().
#   Observati rezultatele.

lista = [1, 45, 88, 34.97, 10000000.0, 'tralala', False, 55]
print("----------------")
print(f"Lista initiala: \n"
      f"{lista}")
print("----------------")

element = lista.pop(5)   # cu functia POP am sters elementul al 6-lea din lista
print(f"Am sters elementul al 6-lea din lista: \n"
      f"{lista}")
print("----------------")

element = lista.remove(88)   # prin functia REMOVE stergem elementul specificat
print(f"Am sters elementul 88 din lista: \n"
      f"{lista}")
print("----------------")



# --------------------------------------------------------------------------------
#7. Numarati elementele dintr-o lista folosind functia len().

lista = [1, 45, 88, 34.97, 10000000.0, 'tralala', False, 55]
print(f"Lista este: {lista}")
print(f"Lista de mai sus are {len(lista)} elemente.")



# --------------------------------------------------------------------------------
#8. Numarati de cate ori apare un anumit element in lista folosind functia count().

lista = [1, 45, 88, 34.97, 10000000.0, 'tralala', False, 55, 45, 1, 1]
print(f"Lista este: {lista}")
element = lista[0]
nr_aparitii = lista.count(element)
print(f"Elementul {element} apare in lista de {nr_aparitii} ori.")



# --------------------------------------------------------------------------------
#9. Uniti doua liste folosind functia extend().

lista1 = [1, 45, 88, 34.97, 10000000.0, 'tralala', False, 55]
lista2 = ['Manolache', True, 'karma', 'generozitate']
print(f"Lista 1 este: {lista1}")
print(f"Lista 2 este: {lista2}")
lista1.extend(lista2)
print(f"Lista 1 rezultata: {lista1}")



# --------------------------------------------------------------------------------
#10. Sortati lista folosind functia sort().

lista = [1, 45, 88, 34.97, 100, 55]
print(f"Lista initiala: {lista}")
lista = sorted(lista)
print(f"Lista sortata: {lista}")



# --------------------------------------------------------------------------------
#11. Inversati continutul listei folosind functia reverse().

lista = [1, 45, 88, 34.97, 100, 55]
print(f"Lista initiala: {lista}")
lista.sort(reverse = True)
print(f"Lista inversata: {lista}")



# --------------------------------------------------------------------------------
#12. Stergeti toate elementele din lista folosind functia clear().

lista = [1, 45, 88, 34.97, 100, 55]
print(f"Lista initiala: {lista}")
lista.clear()
print(f"Lista golita: {lista}")


