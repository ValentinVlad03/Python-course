"""
POLIMORFISMUL = este posibilitatea creării a două funcţii cu nume identic dar cu un comportament diferit.
Polimorfism înseamnă "a avea mai multe forme" şi apare ăn momentul în care folosim moştenirea.
Polimorfismul ne oferă posibilitatea de a folosi metodele moştenite sub mai multe forme, în funcţie de
rezultatul pe care îl dorim.

În limbajul Python implementarea se realizează prin două mecanisme principale: suprascrierea şi
folosirea funcţiei len() şi a operatorilor.
a) suprascriere - două sau mai multe clase pot avea metode cu acelaşi nume, dar comportamentul
acestor metode poate varia în funcţie de tipul obiectelor care le apelează.
"""


class Caine:
    def sunet(self):
        return "Ham, ham!"

class Pisica:
    def sunet(self):
        return "Miau, miau!"

def afiseaza_sunet(animal):     # functia primeste un parametru numit 'animal'.
    print(animal.sunet())       # 'animal' este un obiect de orice tip.
                                # Apoi functia apeleaza metoda 'sunet'.

rex = Caine()
tom = Pisica()

afiseaza_sunet(rex)
afiseaza_sunet(tom)


# -----------------------------------------
# Exemplu de polimorfism cu functie len()

lista = [1, 2, 3, 4, 5]
sir_de_caractere = "Python"

lungime_lista = len(lista)
print(lungime_lista)
lungime_sir = len(sir_de_caractere)
print(lungime_sir)

# Exemplu de polimorfism cu operatorul + (plus)

rezultat1 = 5+7
rezultat2 = "Hello" + " " + "World"
print(rezultat1)
print(rezultat2)

# Exemplu de supraincarcare cu ajutorul unui numar variabil de argumente
# Python nu suporta overloading (supraincarcare) in sensul traditional al limbajelor de programare
# cum ar fi Java sau C++, dar putem avea o forma de supraincarcare prin intermediul valorilor implicite
# ale argumentelor sau a unui numar variabil de argumente
def calculator(*args):
    if len(args) == 1:
        return args[0] * 2
    elif len(args) == 2:
        return args[0] + args[1]
    else:
        return sum(args)

print(calculator(3))
print(calculator(2, 5))
print(calculator(1, 2, 3, 4))

# in functia de mai sus functia 'calculator' accepta un numar variabil de argumente si isi ajusteaza
# comportamentul in functie de numarul acestora.
