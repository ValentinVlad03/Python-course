"""
De rezolvat urmatoarele 2 probleme.
"""


"""
1. Calculare pret discount

Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin 
un copil va avea o reducere de 10%.
Atat pentru seniori cat si pentru non-seniori se va aplica o reducere suplimentara de 10% daca 
vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% 
dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
"""

varsta = int(input("Varsta clientului: "))
nr_copii_insotitori = int(input("Nr. de copii care il insotesc: "))
calatorie_iarna = str(input("Calatoriti iarna (da/nu): "))
calatorie_la_clasa1 = str(input("Calatoriti la clasa 1 (da/nu): "))
calatorie_iarna = calatorie_iarna.lower()
calatorie_la_clasa1 = calatorie_la_clasa1.lower()
reducere = 0

if (varsta > 65):
    reducere = reducere + 0.15
else:
    if (nr_copii_insotitori != 0):
        reducere = reducere + 0.10

if (calatorie_iarna == 'da'):
    reducere = reducere + 0.10

if (calatorie_la_clasa1 == 'da'):
    reducere = reducere - 0.03
else:
    reducere = reducere - 0.01

procent_reducere = reducere * 100
print(f"Reducerea acordata este: {procent_reducere}%.")



# ------------------------------------------------------------------------------------------------

"""
2. Calculare discount seller

Compania X vinde mărfuri la punctele de vânzare cu ridicata și cu amănuntul. Clienții angro primesc 
o reducere de două procente la toate comenzile. De asemenea, compania încurajează atât clienții angro, 
cât și clienții cu amănuntul să plătească ramburs la livrare, oferind o reducere de două procente 
pentru această metodă de plată. Încă o reducere de două procente este acordată pentru comenzile 
de 50 sau mai multe unități. Fiecare coloană reprezintă un anumit tip de ordine.
"""



# ------------------------------------------------------------------------------------------------
"""
3. Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este numele filmului 
vostru preferat. Daca da, atunci printati pe ecran: “Acesta este filmul meu preferat”. In caz contrar 
printati pe ecran: “Din pacate nu este filmul meu preferat"
"""



# ------------------------------------------------------------------------------------------------
"""
4. Aveti la dispozitie urmatorul database url: 
      jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
      
Extrageti din acest text numele bazei de date: mysql.db.server
Folositi un if statement pentru a evalua daca numele bazei de date este 
cel corect (presupunand ca extrageti url-ul dintr-un sistem extern si nu stiti care este acesta)
"""




