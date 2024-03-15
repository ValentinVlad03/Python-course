# --------------------------------------------------------------------------------
# Ex_1 -  Folosește funcția print() și printează în consola 4 propoziții folosind
# cele 4 variabile. Rezolvă nepotrivirile de tip pe rand prin toate modalitatile cunoscute



# --------------------------------------------------------------------------------
# Ex_2 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le
# in cate o variabila. Afișează pe ecran următoarea propoziție:
# 'Numele complet are x caractere'.

prenume = str(input("Prenumele : "))
nume = str(input("Numele : "))
nr_caractere = len(prenume) + len (nume)
print(f"Numele complet are {nr_caractere} caractere.")



# --------------------------------------------------------------------------------
# Ex_3 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le
# in cate o variabila. Afișează pe ecran următoarea propoziție:
# 'Aria dreptunghiului este x'.

lungime = float(input("Dreptunghiul are lungimea de: "))
latime = float(input("Dreptunghiul are latimea de: "))
aria_dreptunghiului = lungime * latime
aria_dreptunghiului = round(aria_dreptunghiului, 2)  # am rotunjit ca sa afiseze doar doua cifre dupa virgula
print(f"Aria dreptunghiului este: {aria_dreptunghiului} mp.")



# --------------------------------------------------------------------------------
# Ex_4 - Având string-ul: 'Coral is either the stupidest animal or the smartest rock'
# afișează de câte ori apare cuvântul 'the' în acest string.

paragraf = "Coral is either the stupidest animal or the smartest rock"
nr_de_aparitii = paragraf.count("the")
print(f"Textul de analizat: {paragraf}")
print(f"Cuvantul <<the>> apare de {nr_de_aparitii} ori in textul de mai sus.")



# --------------------------------------------------------------------------------
# Ex_5 - Folosindu-te de string-ul de la exercițiul 8, inlocuieste “the” cu “THE”
# peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul.

paragraf = "Coral is either the stupidest animal or the smartest rock"
paragraf_nou = paragraf.replace("the", "THE")
print(f"Textul de analizat: {paragraf}")
print(f"Am inlocuit cuvantul <<the>> cu <<THE>> in textul de mai sus.")
print(f"Textul rezultat este: {paragraf_nou}")



# --------------------------------------------------------------------------------
#Ex_6 Folosindu-te de string-ul de la exercițiul 8 foloseste un assert ca să
# verifici dacă acest string conține doar numere.
