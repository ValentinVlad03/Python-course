# --------------------------------------------------------------------------------
# Ex_1 Explica cu cuvintele tale in cadrul unui comentariu cum
# functioneaza un << if else >>.




# --------------------------------------------------------------------------------
# Ex_2 Verifica si afiseaza daca x este numar natural sau nu (un numar se
# considera natural daca este numar intreg mai mare ca 0).

x = float(input("Numar: "))
partea_intreaga = round(x)
if (x > 0) and ((x / partea_intreaga) == 1):
    print(f"Numarul {x} este un numar natural.")
else:
    print(f"Numarul {x} nu este un numar natural.")



# --------------------------------------------------------------------------------
# Ex_3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru.

x = float(input("Numar: "))
if (x > 0) :
    print(f"Numarul {x} este pozitiv.")
if (x == 0) :
    print(f"Numarul {x} este nul (neutru).")
if (x < 0) :
    print(f"Numarul {x} este negativ.")



# --------------------------------------------------------------------------------
# Ex_3 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

x = float(input("Numar: "))
if (x >= -2) and (x <= 13):
    print(f"Numarul de mai sus este in intervalul [-2, 13].")
else:
    print(f"Numarul de mai sus nu este in intervalul [-2, 13].")



# --------------------------------------------------------------------------------
# Ex_4 Verifica daca x NU este intre 5 si 27, excluzand capetele de interval.
# (a se folosi ‘not’)

x = float(input("Numar: "))
if not ((x > 5) and (x < 27)):
    print(f"Numarul de mai sus nu este in intervalul [5, 27], excluzand capetele de interval.")
else:
    print(f"Numarul de mai sus este in intervalul [5, 27], excluzand capetele de interval.")



# --------------------------------------------------------------------------------
# Ex_5 Declara o noua variabila y de tip int si apoi verifica si afiseaza
# daca # x si y sunt egale, daca nu, afiseaza care din ele este mai mare.

x = float(input("introduceti valoarea lui x: "))
y = int(input("introduceti valoarea lui y: "))
if (x == y):
    print("Cele doua numere sunt egale.")
else:
    if (x > y):
        print(f"Numarul x este mai mare decat y.")
    else:
        print(f"Numarul y este mai mare decat x.")



# --------------------------------------------------------------------------------
# Ex_6 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi,
# afiseaza daca triunghiul este isoscel (doua laturi sunt egale), echilateral
# (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).

print("Introduceti mai jos lungimile laturilor triunghiului.")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if ((x == y) and (y == z)):
    print("Triunghiul este echilateral.")
else:
    if (x == y) or (x == z) or (y == z):
        print("Triunghiul este isoscel.")
    else:
        print("Triunghiul este oarecare (are laturile inegale).")



# --------------------------------------------------------------------------------
# Ex_7 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala
# sau nu. Atentie! Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

litera = input("Introduceti litera: ")

# daca introduce mai multe litere atunci sa imi ia in considerare doar prima litera.
if (len(litera) > 1):
    litera = litera[0]
    print(f"Litera aleasa este: '{litera}'")

vocale = ['a', 'A', 'e', 'E', 'o', 'O', 'u', 'U', 'i', 'I', 'ă', 'Ă', 'î', 'Î', 'â', 'Â']
if vocale.__contains__(litera):
    print("Litera este o vocala.")
else:
    print("Litera aleasa nu este o vocala.")