# ---------------------------------------------------------------------------
"""
Definiti o adresa de memorie care sa salveze data curenta. Va fi o variabila sau o constanta?
"""

data_curenta = input("Data curenta este: ")
print(f"Tipul de data al variabilei {data_curenta} este: datetime.")
# [Vali]: Este o variabila, dar nu stiu cum sa o formatez... ca sa apara ca fiind de tip datetime, nu str.
# [Vali]: Nu am inteles de ce primul comentariu, cel cu <Definiti o adresa...> mi l-a scris cu font italic.



# ----------------------------------------------------------------------------
"""
Identificati tipul de data pe care il are variabila pe care ati definit-o 
folosind una din functiile invatate la curs.
"""
print(type(data_curenta))



# ----------------------------------------------------------------------------
"""
Definiti alte cateva variabile care sa stocheze cursul la care sunteti, ce zi 
este si la ce sesiune de curs sunteti.
"""

cursul_la_care_sunt = str(input("Acum urmez cursul de: "))
data_de_azi = str(input("Ce zi este astazi? \n adica in ce data suntem: "))
sesiune_curenta = str(input("Ce sesiune de curs urmezi acum: "))

# [Vali]:
# ----------------------------------------------------------------------------
"""
Salvati fiecare cuvant din propozitia: “Ana s-a nascut in anul 1990 si acum 
are 33 de ani” in cate o adresa de memorie.
"""

text = "Ana s-a nascut in anul 1990 si acumare 33 de ani"
print(f"Asa impartim sirul de caractere dupa spatii  {text.split()}")
data = "22-11-2023"
print(f'Asa facem split cu argument: {data.split("-")}')

# ----------------------------------------------------------------------------
"""
Printati propozitia de mai sus folosind trei tipuri diferite de printuri.
"""

# ----------------------------------------------------------------------------
"""
Declarati cateva alte adrese de memorie la alegere si initializati-le folosind 
functia input.
"""

# ----------------------------------------------------------------------------
"""
Adaugati comentarii la fiecare linie de cod cu explicatii cu privire la ce 
ati facut la fiecare.
"""
