# Xpath

# Xpath = este de doua tipuri:
#  -  xpath absolut = o adresa completa incepand de la inceputul paginii si desfasurat din parinte
#                     in copil pana la elementul cautat. Atunci cand se face cautare dupa xpath absolut
#                       se foloseste caracterul '/'
#  - xpath relativ = o adresa partiala incepand cu primul element identificat pe pagina si desfasurat din
#                    parinte in copil, sau din copil in parinte, sau din frate in frate pana la identificarea
#                    elementului cautat.  Atunci cand se face cautare de xpath relativ se foloseste '//'



# ---------------------

# Cautare dupa atribut-valoare pentru un tag specific
# Exemplu>  //button   --- sistemul va cauta toate elementele de pe site care au tag-ul 'button'

# cautare dupa atribut-valoare. Atunci cand facem cautare dupa atribut-valoare, atributul trebuie precedat intotdeauna
# de caractarul @ .
# De asemenea, se va plasa perechea cheie-valoare intre paranteze '[]'.
# Exemplu:   //button[@class = 'navbar-toggler'] --> sistemul va cauta toate elementele care au tagul button si perechea
# atribut-valoare (in cazul nostru atributul este 'class' iar valoare este 'navbar-toggler').

# atunci cand nu stim sau nu ne intereseaza tag-ul, putem faca cautare dupa atribut-valoare prin intermediul
# caracterului '*', Acest caracter este echivalentul lui ALL (tot).
# Exemplu:   //*[@class = 'navbar-toggler']

# !!! Atentie la XPATH daca avem clase care au valoarea formata din elemente separate prin spatiu, atunci TREBUIE sa le
# punemm pe toate.
# Exemplu:    //*[@class = 'navbar navbar-expand-lg bg-light']

# cautare dupa copil prin navigare in jos --> ne folosim de operatorul '/'

# Exemplu:   sa presupunem ca avem un HTML de genul:
"""
<div id = 'parinte'>
     <p>Primul paragraf </p>
     <p>Primul paragraf </p>
</div>

daca vrem sa selectam al 2-lea paragraf construim Xpath-ul ca mai jos
//div[@id = 'parinte']/p[2]
"""


from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

# chrome.get('https://formy-project.herokuapp.com/scroll')

# cautarea cu Xpath folosindu-ne la constructia Xpath-ului de doua conditii (ambele sunt adevarate)
# chrome.find_element()


"""
sa zicem ca avem un cod HTML de genul:
<div class = 'clasa1'>Element cu clasa 1</div>
<div class = 'clasa2'>Element cu clasa 2</div>

Construim Xpath-ul ca sa ne aduca toate div-urile care sunt cu clasa1 si clasa2

//div[@class = 'clasa1'] | //div[@class = 'clasa2']
sau
//div[@class = 'clasa1' or @class = 'clasa2']

cautare cu OR doar a doua conditie adevarata

//div[contains(@class, 'clasa1') or contains(@class, 'clasa2')]

"""


# cautare Xpath dupa text
chrome.get('https://formy-project.herokuapp.com/javascripts_alerts')
chrome.find_element(By.XPATH, "//button[text() = 'Click for JS Alert']").click()
sleep(3)


"""
navigarea pe axa x si y
1. Navigarea din parinte in copil se face cu caracterul /
ex. //div/p

2. navigarea catre un urmas care nu este urmasul direct: ne folosim de //.
ex. //div/p//input

3. Navigare in sus catre parinte se face cu '//parent::tag'
ex. //p/parent::div    --- specifica sa selectam parintele nodului curent care are eticheta div

4. Navigare la urmatorul frate cu '/following-sibling::tag'
Ex.   //div/following-sibling::p

5. Navigare la fratele anterior cu '/preciding-sibling::tag'
Ex.   //p/preceding-sibling::p



"""