# Definiti o lista care sa stocheze numele tuturor celor prezenti la studiul individual.
# Parcurgeti lista si printati toate elementele din aceasta folosind pe rand for, while si foreach

lista_prezenta = ["Ivan Cristina","Dogaru Valentin","Runcanu Irina","Moraru Alexandru","Borbey Robert","Raduleanu Serban"]
nr_persoane = len(lista_prezenta)

print(" -------- ciclul FOR ------------")
for i in range(0,nr_persoane):
    print(lista_prezenta[i])

print(" -------- ciclul WHILE ------------")
i = 0
while i < nr_persoane :
    print(f"{lista_prezenta[i]}")
    i += 1

print(" -------- ciclul FOR EACH ------------")
for element in lista_prezenta:
    print(element)



# -----------------------------------------------------------------------------------------------
# Exercitii bonus - ATENTIE!!! Pentru aceste exercitii va trebui sa va puneti in aplicare
# abilitatile de “detectivi” si sa cautati pe google

# Bonus 1: Sortati o lista folosind algoritmul de sortare prin metoda bulelor (bubble sort)

lista = [1, 5, 2, 9, 14, 11, 8, 24, 19, 20, 15, 30]
print("----------------------------------------------------------------")
print(f"Lista initiala: {lista}")
print("----------------------------------------------------------------")
nr_elemente = len(lista)
i = 0   # contor primar
j = 0   # contor secundar, pentru ca avem nevoie ca lista sa fie parcursa
        # complet de un numar de ori egal cu numarul de elemente

for i in range(0, nr_elemente):
    for j in range(0, nr_elemente-1):
        if lista[j] > lista[j+1]:       # daca un element e mai mare ca urmatorul
                                        # atunci le interschimbam valorile
             buffer =  lista[j+1]
             lista[j+1] = lista[j]
             lista[j] = buffer

print(f"Lista sortata:  {lista}")
print("----------------------------------------------------------------")



# -----------------------------------------------------------------------------------------------
# Bonus 2: Incercati sa printati pe ecran pe cei 101 dalmatieni salvati intr-o lista.
#          La fiecare dalmatian veti printa pe ecran urmatorul text:
#          “Dalmatianul curent se afla in pozitia “i””.
#          Atentie, ghilimelele vor trebui tratate folosind caracterul escape.
