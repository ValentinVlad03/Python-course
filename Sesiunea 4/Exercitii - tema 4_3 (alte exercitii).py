# --------------------------------------------------------------------------------
# 1.  Ascunde vocalele! Să se scrie un "translator" care să modifice
#     vocalele în "*" utilizând ciclul while / if / for.

vocale = ['a', 'A', 'e', 'E', 'o', 'O', 'u', 'U', 'i', 'I', 'ă', 'Ă', 'î', 'Î', 'â', 'Â']
text = str(input("Introduceti textul: "))
lungime_text = len(text)

print(f"----------- ciclu FOR -------------")
text_rezultat = ''
for i in range(0, lungime_text):
    if text[i] in vocale:
        text_rezultat += '*'
    else:
        text_rezultat += text[i]
print(text_rezultat)

print(f"----------- ciclu WHILE -------------")
text_rezultat = ''
i=0
while i < lungime_text:
    if text[i] in vocale:
        text_rezultat += '*'
    else:
        text_rezultat += text[i]
    i += 1
print(text_rezultat)



# --------------------------------------------------------------------------------
# 2.  Tipăriţi toate numerele prime aflate între două numere naturale
#     citite de la tastatura.

numar1 = int(input("Primul numar: "))
numar2 = int(input("Al 2-lea numar: "))

for nr_intermediar in range(numar1, numar2+1):

    # verificam daca nr_intermediar este numar prim
    nu_e_nr_prim = False
    if nr_intermediar > 1:
        for i in range(2, nr_intermediar):
            if ((nr_intermediar % i) == 0):
                nu_e_nr_prim = True
                break
    if not nu_e_nr_prim:
        print(f"Numar prim: {nr_intermediar}")



# --------------------------------------------------------------------------------
# 3.  Se citește un număr natural n.
#     Să se scrie programul care determină și afișează câte cifre impare are numărul citit.

numar = input("Numarul este: ")
nr_cifre_impare = 0
i = 0
nr_caractere = len(numar)
for i in range(0,nr_caractere):
    if numar[i].isnumeric():                    # verifica daca e cifra. Atentie, sa nu fie virgula...
        cifra = int(numar[i])
        if not ((cifra % 2) == 0):              # verifica daca cifra e impara
             nr_cifre_impare += 1
if nr_cifre_impare > 0:
    print(f"Numarul {numar} are {nr_cifre_impare} cifre impare.")
else:
    print(f"Numarul {numar} nu are cifre impare.")

# --------------------------------------------------------------------------------
# 4.  Se citește un număr natural n.
#     Să se scrie programul care determină și afișează numărul de cifre ale lui n.

numar = input("Numarul este: ")
nr_cifre= 0
i = 0
nr_caractere = len(numar)
for i in range(0,nr_caractere):
    if numar[i].isnumeric():
        cifra = int(numar[i])
        nr_cifre += 1
if nr_cifre > 0:
    print(f"Numarul {numar} are {nr_cifre} cifre.")
else:
    print(f"Sigur ati tastat un numar ?.")



# --------------------------------------------------------------------------------
# 5.  Se citește un număr natural n.
#     Să se scrie programul care verifică dacă numărul se citește palindrom.

numar = input("Numarul: ")
nr_caractere = len(numar)
i = 0
nr_inversat = ''

for i in range(0, nr_caractere):
    cifra = numar[nr_caractere - i - 1]
    nr_inversat += cifra

print(f"Numarul inversat este: {nr_inversat}")

if nr_inversat == numar:
    print(f"Numarul {numar} este palindrom.")
else:
    print(f"Numarul {numar} nu este palindrom.")



# --------------------------------------------------------------------------------
# 6.  Se citește un număr natural n.
#     Să se scrie programul care determină și afișează cea mai mare
#     și cea mai mică cifră a numărului n.

numar = input("Numar: ")
nr_cifre  = len(numar)
cifra_max = int(numar[0])
cifra_min = int(numar[0])
i = 0    # contor general
j = 0    # contor pentru cifrele citite pana acum, pana la pozitia curenta
print(f"Numar cifre: {nr_cifre}")

for i in range(1, nr_cifre):
   cifra_curenta = int(numar[i])
   if i >0:
        for j in range(0, i):
             if cifra_curenta >= cifra_max:
                    cifra_max = cifra_curenta
             if cifra_curenta <= cifra_min:
                    cifra_min = cifra_curenta

print(f"Cifra minima a numarului este: {cifra_min}")
print(f"Cifra maxima a numarului este: {cifra_max}")



# --------------------------------------------------------------------------------
# 7.  Se citește un număr natural n.
#     Să se scrie programul care afișează pe ecran mesajul DA dacă toate
#     cifrele lui n sunt în ordine crescătoare și mesajul NU în caz contrar.

numar = input("Numar: ")
nr_cifre  = len(numar)
crescator = False
descrescator = False
cifra_anterioara = int(numar[0])
i = 0        # contor general
print(f"Numar cifre: {nr_cifre}")


# definim un ciclu FOR pentru a vedea daca ordinea este crescatoare
for i in range(1, nr_cifre):
   cifra_curenta = int(numar[i])
   if cifra_curenta >= cifra_anterioara:
        cifra_anterioara = cifra_curenta
        crescator = True
   else:
        crescator = False
        break

# definim un ciclu FOR pentru a vedea daca ordinea este descrescatoare
for i in range(1, nr_cifre):
   cifra_curenta = int(numar[i])
   if cifra_curenta <= cifra_anterioara:
        cifra_anterioara = cifra_curenta
        descrescator = True
   else:
        descrescator = False
        break

if crescator:
    print(f"Numarul de mai sus are cifrele in ordine crescatoare.")
if descrescator:
    print(f"Numarul de mai sus are cifrele in ordine descrescatoare.")
if (not crescator) and (not descrescator):
    print("Numarul precizat mai sus nu are cifrele ordonata crescator sau descrescator.")



# --------------------------------------------------------------------------------
# 8.  Se citesc n numere întregi.
#     Se cere:
#      -- suma numerelor citite,
#      -- maximul, minimul,
#      -- cele mai mari/mai mici două numere citite,
#      -- câte sunt negative,
#      -- câte sunt pare/impare,
#      -- cel mai mare număr negativ/pozitiv.

