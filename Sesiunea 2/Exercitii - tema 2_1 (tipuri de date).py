# --------------------------------------------------------------------------------
# Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.

# Variabila este o adresa de memorie care stocheaza valori,
# aceste valori putand fi modificate pe parcussul executiei codului.


# --------------------------------------------------------------------------------
# Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele
# tipuri: int, string, float, boolean


# evidenta cladiri de birouri de administrat
nume_complet = str(input("Numele cladirii : "))
an_constr = int(input("Anul dării în folosinţă : "))
supraf_desf = float(input("Suprafata desfasurata inchiriabila [mp]: "))
contract_inchiriere = bool(input("Este inchiriata cladirea:"))



# --------------------------------------------------------------------------------
# Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate
# mai sus au tipul de date așteptat.

print(type(nume_complet))
print(type(an_constr))
print(type(supraf_desf))
print(type(contract_inchiriere))


# --------------------------------------------------------------------------------
# Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această
# modificare în aceeași variabilă (suprascriere),
# apoi verifică din nou tipul de date al acesteia.

supraf_desf = round(supraf_desf)
print(type(supraf_desf))
# deci se transforma din float in int.


# --------------------------------------------------------------------------------
# Ex_5 - Incearca sa convertesti variabila string la int folosind type casting si
# observa rezultatele

an_declarat = "1978"
an_int = int(an_declarat)
an_curent = 2023
varsta = an_curent - an_int
print(f"Ati declarat ca v-ati nascut in {an_int}, deci aveti {varsta} ani.")

# --------------------------------------------------------------------------------
# Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si
# observa rezultatele

o_noua_masina_este_parcata = True
nr_masini_parcate = 10
if o_noua_masina_este_parcata:
    nr_masini_parcate += int(o_noua_masina_este_parcata)
    print(f"Acum sunt {nr_masini_parcate} active.")
else:
    print(f"A ramas acelasi numar de parcari, adica {nr_masini_parcate} locuri de parcare.")



# --------------------------------------------------------------------------------
# Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in
# true) si repeta exercitiul anterior.


o_noua_masina_este_parcata = False
nr_masini_parcate = 10
if o_noua_masina_este_parcata:
    nr_masini_parcate += int(o_noua_masina_este_parcata)
    print(f"Acum sunt {nr_masini_parcate} locuri de parcare ocupate.")
else:
    print(f"A ramas acelasi numar de parcari ocupate, adica {nr_masini_parcate} locuri de parcare.")