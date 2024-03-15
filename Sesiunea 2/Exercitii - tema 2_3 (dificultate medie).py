# --------------------------------------------------------------------------------
# Ex_1 Citește de la tastatură un string de dimensiune impară și afișează
# caracterul din mijloc.

print("Trebuie introdus un text care are un numar impar de caractere.")
text_de_analizat = str(input("Textul de analizat: "))
lungime_text = len(text_de_analizat)
if lungime_text % 2 == 0:
    print("Textul are un numar par de caractere. Deci nu respecta conditia.")
else:
    pozitia_centrala = int(lungime_text/ 2)
    caracterul_din_mijloc = text_de_analizat[pozitia_centrala]
    print(f"Textul are {lungime_text} caractere.")
    print(f"Caracterul din mijloc este: '{caracterul_din_mijloc}'.")



# --------------------------------------------------------------------------------
# Ex_2 Folosind assert, verifică dacă un string este palindrom.

text_de_analizat = str(input("Textul de analizat: "))
textul_inversat = ""
palindrom = True
contor = 1
lungime_text = len(text_de_analizat)
for contor in range(1,lungime_text+1):
    textul_inversat = textul_inversat + text_de_analizat[lungime_text - contor]

print(f"Textul inversat este: {textul_inversat}")
if textul_inversat == text_de_analizat:
    print("Textul este palindrom.")
    palindrom = True
else:
    print("Textul introdus nu este palindrom.")
    palindrom = False

# ???? cum folosim functia assert in cazul asta ???
# poti sa faci verificarea folosind textul palindrom:   SATOR AREPO TENET OPERA ROTAS
assert(palindrom)



# --------------------------------------------------------------------------------
# Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia
# sa efectuezi urmatoarele:
#     - salvează fiecare cuvânt într-o variabilă;
#     - printează ambele variabile pentru verificare.

text_de_analizat = str(input("Textul de analizat: "))
cuvant = str(text_de_analizat.split(" "))
print(cuvant)



# --------------------------------------------------------------------------------
# Ex_4 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia
# sa efectuezi urmatoarele:
#     - salvează primul caracter într-o variabilă
#     - capitalizează acest caracter peste tot, mai puțin pentru
#       primul și ultimul caracter => alAbAlA portocAla.

text_de_analizat = str(input("Textul de analizat: "))
primul_caracter = text_de_analizat[0]
textul_rezultat = primul_caracter
lungime_text = len(text_de_analizat)
contor = 1
for contor in range(1,lungime_text):
    caracter_curent = text_de_analizat[contor]
    if (caracter_curent == primul_caracter) and (contor <= (lungime_text - 2)):
        textul_rezultat += text_de_analizat[contor].upper()
    else:
        textul_rezultat += text_de_analizat[contor]
print(f"Textul rezultat este: {textul_rezultat}")

# incearca sa testezi daca merge si cu textul :  "procesul de promovare perpetua la un izotop"



# --------------------------------------------------------------------------------
# Ex_5 - citeste un user de la tastatura, citeste o parola.
# Afiseaza: 'Parola pt user x este ***** si are x caractere'.

user = str(input("User: "))
parola = str(input("Parola: "))
i = 1
lungime_parola = len(parola)
stelute = "*"
for i in range(1, lungime_parola):
    stelute += "*"
print(f"Parola ptr. userul {user} este {stelute} si are {lungime_parola} caractere.")
