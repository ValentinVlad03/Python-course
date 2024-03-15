"""

Intrati pe site-ul https://www.elefant.ro/ si efectuati urmatoarele teste:

#Test 1: Identificati butonul "accept cookies" si dati click pe el

#Test 2: cautati un produs la alegere (iphone 14) si
         verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])

#Test 3: Extrageti din lista produsul cu pretul cel mai mic
         [class="current-price "] -> //img[@class="product-image"]

#Test 4: Extrageti titlul paginii si verificati ca este corect

#Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
         Identificati elementele de tip user si parola si inserati valori incorecte
         (valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)

#Test 6: Dati click pe butonul "conectare" si verificati urmatoarele:
            1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta

#Test 7: Stergeti valoarea de pe campul email si introduceti o valoare invalida
         (adica fara caracterul "@"), fara sa introduceti si parola si verificati
         faptul ca butonul de login este dezactivat.

"""



# importam bibliotecile de functii

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----------------------------------------------------------------------------------------------------------------
# Test 1: Identificati butonul "accept cookies" si dai click pe el.

# initializan Chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# intrăm pe site:
chrome.get('https://www.elefant.ro/')
sleep(3)

# dam click pe butonul de acceptare a cookie-urilor
chrome.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
chrome.maximize_window()
sleep(1)


# -----------------------------------------------------------------------------------------------------------------
# Test 2: cautati un produs la alegere (iphone 14) si
#         verificati ca s-au returnat cel putin 10 rezultate.
#         ([class="product-title"])

produs_cautat = 'iphone 14'
chrome.find_element(By.XPATH,'/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/input[1]').click()
sleep(1)
chrome.find_element(By.XPATH,'/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/input[1]').send_keys(produs_cautat)
sleep(1)
chrome.find_element(By.XPATH, '/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/button/span').click()
sleep(1)

# ???????????????? tot nu am reuşit să număr rezultatele afişate/găsite....



# -----------------------------------------------------------------------------------------------------------------
# Test 3: Extrageti din lista produsul cu pretul cel mai mic
#         [class="current-price "] -> //img[@class="product-image"]

chrome.find_element(By.ID, 'SortingAttribute').click()
sleep(1)
chrome.find_element(By.CSS_SELECTOR, '#SortingAttribute > option:nth-child(4)').click()
sleep(1)

nume_produs = chrome.find_element(By.CSS_SELECTOR, '.js-product-tile-33133486-edd4-48c4-a7f9-dc3593fe8ae8 > div:nth-child(2) > a:nth-child(3)').text
print(f'----------------------------------------------')
print(f'Produsul cu pretul cel mai mic din lista este: ')
print(f'>>> {nume_produs} <<<')
print(f'----------------------------------------------')



# -----------------------------------------------------------------------------------------------------------------
# Test 4: Extrageti titlul paginii si verificati ca este corect.

titlu_corect = 'Cauti iphone 14? - Vino pe Elefant.ro!'
titlu_gasit  = chrome.title
try:
    assert titlu_gasit == titlu_corect
    print('Titlul paginii este corect.')
    print(f'>>> ' + titlu_gasit + ' <<<')
except:
    print('Titlul paginii este incorect.')
    print(f'Cautam ca titlul sa fie >>> {titlu_corect}')
print(f'----------------------------------------------')



# -----------------------------------------------------------------------------------------------------------------
# Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
#        Identificati elementele de tip user si parola si inserati valori incorecte
#        (valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)

chrome.get('https://www.elefant.ro/')
# dam clic pe butonul "Conectare" de pe pagina
chrome.find_element(By.CSS_SELECTOR,'.login-prompt').click()
sleep(1)
            # neaparat mereu sa introduci o pauza (sleep...) dupa ce dai clic daca
            # urmeaza sa se deschida o fereastra de dialog
            # ca sa aibe timp serverul sa raspunda si site-ul sa se incarce

# apoi clic pe butonul "Conectare" din fereastra cu optiunile de conectare pe cont
chrome.find_element(By.XPATH,'/html/body/header/div[1]/nav/div/div[4]/div/ul/li[1]/div[2]/a[1]').click()
# apoi dam clic in casuta de introducere a emailului
chrome.find_element(By.CSS_SELECTOR, '#ShopLoginForm_Login').send_keys('bla-bla')
sleep(1)
# apoi dam clic in casuta de introducere a parolei
chrome.find_element(By.CSS_SELECTOR, '#ShopLoginForm_Password').send_keys('bla-bla')
sleep(1)

print(f'-----------------------------------------------------------------------')
print(f'Gata. Am introdus valori incorecte in campurile pentru email si parola.')
print(f'-----------------------------------------------------------------------')



# -----------------------------------------------------------------------------------------------------------------
# Test 6: Dati click pe butonul "conectare" si verificati urmatoarele:
#            1. Faptul ca nu s-a facut logarea in cont
#            2. Faptul ca se returneaza eroarea corecta.

        # memoram adresa URL la care suntem inainte de a ne conecta
adresa_curenta = chrome.current_url
        # dam click pe butonul "Conectare"
chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button').click()
sleep(1)
adresa_dupa_click_conectare = chrome.current_url      # memoram adresa URL la care suntem dupa ce am dat click
if adresa_curenta == adresa_dupa_click_conectare:
    print(f'Am ramas pe aceeasi pagina de site. Deci nu s-a facut logarea pe cont.')
else:
    print(f'Am plecat de pe pagina respectiva. Deci m-am logat pe cont.')


# verificam faptul ca butonul "Conectare" este dezactivat, deci ca nu s-a facut logarea pe cont
codul_elementului = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button').get_attribute('outerHTML')
marcaj_dezactivare = 'disabled="disabled"'
if marcaj_dezactivare in codul_elementului:
    print (f'Butonul "Conectare" este dezactivat.')
else:
    print(f'Butonul "Conectare" este activat.')

# verificam faptul ca se returneaza mesajul de eroare corect.
mesaj_eroare_email_gresit = 'Te rugăm să introduci o adresă de e-mail validă.'
print(f'Aştept să se afişeze mesajul de eroare: <<{mesaj_eroare_email_gresit}>>')
localizare_mesaj_eroare = chrome.find_element(By.XPATH,'/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[1]/div/small[1]')
sleep(1)

try:
    asteptare_eroare = WebDriverWait(chrome,3).until(EC.visibility_of(localizare_mesaj_eroare))
    assert asteptare_eroare.is_displayed()
    print('Mesajul de eroare este afisat.')
except AssertionError:
    print('Mesajul de eroare nu este afisat.')

print(f'-----------------------------------------------------------------------')




# -----------------------------------------------------------------------------------------------------------------
# Test 7: Stergeti valoarea de pe campul email si introduceti o valoare invalida
#         (adica fara caracterul "@"), fara sa introduceti si parola si verificati
#         faptul ca butonul de login este dezactivat.


chrome.find_element(By.CSS_SELECTOR, '#ShopLoginForm_Login').clear()
chrome.find_element(By.CSS_SELECTOR, '#ShopLoginForm_Login').send_keys('Portocale_albastre')
sleep(1)
codul_elementului = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button').get_attribute('outerHTML')
marcaj_dezactivare = 'disabled="disabled"'
if marcaj_dezactivare in codul_elementului:
    print (f'Butonul "Conectare" este dezactivat.')
else:
    print(f'Butonul "Conectare" este activat.')

chrome.quit()