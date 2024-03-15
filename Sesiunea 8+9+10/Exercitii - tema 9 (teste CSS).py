"""

# - Test 1: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
#            cel putin 10 rezultate  ([class="product-title"])

# - Test 2: faceti filtrare dupa pret si verificati faptul ca toate produsele returnate
#            au pretul in intervalul de filtrare

# - Test 3: Cautati un produs care nu exista si verifica faptul ca mesajul returnat este:
#            "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."

# - Test 4: Cautati un produs, sortati lista de rezultate in ordine crescatoare dupa pret
#            si verificati faptul ca produsele au fost intr-adevar sortate

# - Test 5: Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare
#            dupa pret si verifica faptul ca produsele au fost intr-adevar sortate.

# - Test 6: Intrati pe elefant.ro, dati click pe linkul Contact, si verificati faptul
#            ca nu puteti sa dati submit la formular daca nu sunt completate campurile obligatorii
#            (verificati ca ramaneti pe aceeasi pagina) (hint: folositi metoda current_url)

"""


# importam bibliotecile de functii

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# initializan Chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# intrăm pe site:
chrome.get('https://www.elefant.ro/')
sleep(1)
chrome.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
chrome.maximize_window()
sleep(1)



# -----------------------------------------------------------------------------------------------------------------
# - Test 1: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate

produs_cautat = 'iphone 14'
chrome.find_element(By.XPATH,'/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/input[1]').click()
sleep(1)
chrome.find_element(By.XPATH,'/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/input[1]').send_keys(produs_cautat)
sleep(1)
chrome.find_element(By.XPATH, '/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/button/span').click()
sleep(3)

text_afisat = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div[14]/div[2]/div[2]/div/div[2]/div[2]').text
        # definim o functie for prin care extragem partea numerica din "215 produse" gasite
text_numeric = ''
for i in range(0,(len(text_afisat)-8)):
    text_numeric += text_afisat[i]
numar_produse_gasite = int(text_numeric)
print(f"Numar de produse gasite: {numar_produse_gasite}")
        # verificam daca au fost gasite mai mult de 10 produse, adica avem mai mult de 10 rezultate
limita_inferioara = 10
if numar_produse_gasite > limita_inferioara:
    print(f"Au fost gasite mai mult de {limita_inferioara} produse ce corespund criteriului de cautare.")
else:
    print(f"Nu au fost returnate suficiente rezultate in urma cautarii.")



# -----------------------------------------------------------------------------------------------------------------
# - Test 2: Faceti filtrare dupa pret si verificati faptul ca toate produsele returnate
#           au pretul in intervalul de filtrare

# ??????????????


# -----------------------------------------------------------------------------------------------------------------
# - Test 3: Cautati un produs care nu exista si verifica faptul ca mesajul returnat este:
#            "Nu a fost găsit niciun rezultat :"

produs_cautat = 'aaaabbbcccc'
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/input[1]').send_keys(produs_cautat)
sleep(1)
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button/span').click()
sleep(1)
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button/span').click()
sleep(1)

        # se verifica faptul ca da mesaj de eroare daca se introduce un produs care nu exista in baza de date
mesaj_afisat = chrome.find_element(By.CLASS_NAME,'no-search-result').text
mesaj_cautat = 'Nu a fost găsit nici un rezultat :'
try:
    mesaj_cautat = mesaj_afisat
    print('Mesaj corect.')
except :
    print('Mesaj incorect. Mesajul nu corespunde cu ceea ce se aştepta!')




# -----------------------------------------------------------------------------------------------------------------
# - Test 4: Cautati un produs, sortati lista de rezultate in ordine crescatoare dupa pret
#            si verificati faptul ca produsele au fost intr-adevar sortate

produs_cautat = 'telefon nokia'
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/input[1]').send_keys(produs_cautat)
sleep(1)
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button/span').click()
sleep(1)
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button/span').click()
sleep(1)
chrome.find_element(By.ID, 'SortingAttribute').click()
chrome.find_element(By.CSS_SELECTOR, '#SortingAttribute > option:nth-child(4)').click()
sleep(5)

# cum verificam ca e sortata lista crescator ????



# -----------------------------------------------------------------------------------------------------------------
# - Test 5: Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare
#            dupa pret si verifica faptul ca produsele au fost intr-adevar sortate.

produs_cautat = 'telefon nokia'
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/input[1]').send_keys(produs_cautat)
sleep(1)
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button/span').click()
sleep(1)
chrome.find_element(By.XPATH,'//*[@id="HeaderRow"]/div[4]/div/div[1]/form/button/span').click()
sleep(1)
chrome.find_element(By.ID, 'SortingAttribute').click()
chrome.find_element(By.CSS_SELECTOR, '#SortingAttribute > option:nth-child(5)').click()
sleep(5)

# cum verificam ca e sortata lista descrescator ????



# -----------------------------------------------------------------------------------------------------------------
# - Test 6: Intrati pe elefant.ro, dati click pe linkul Contact, si verificati faptul
#            ca nu puteti sa dati "Trimite" la formular daca nu sunt completate campurile obligatorii
#            (verificati ca ramaneti pe aceeasi pagina) (hint: folositi metoda current_url)

        # intram pe pagina "Contact" a saitului.
chrome.find_element(By.CSS_SELECTOR, '#Pagelet_19MKKgAHpJUAAAFmiq0Nuosl > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)').click()
sleep(3)
adresa_curenta = chrome.current_url
        # dam clic pe butonul "Trimite"
chrome.find_element(By.CSS_SELECTOR, '.o-btn').click()
sleep(1)
        # memoram adresa URL la care suntem dupa ce am dat clic
adresa_dupa_clicktrimite = chrome.current_url

if adresa_curenta == adresa_dupa_clicktrimite:
    print(f'Am ramas pe aceeasi pagina de site.')
else:
    print(f'Am plecat de pe pagina respectiva.')

