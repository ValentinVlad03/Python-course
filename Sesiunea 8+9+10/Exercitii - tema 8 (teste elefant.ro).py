"""
# - Test 1: Intrati pe site-ul https://www.elefant.ro/

# - Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
            cel putin 10 rezultate
            ([class="product-title"])

# - Test 3: Extrageti din lista produsul cu prețul cel mai mic [class="current-price "]
            (puteti sa va folositi de find_elements)

# - Test 4: Extrageti titlul paginii si verificati ca este corect (hint: folositi metoda title)

# - Test 5: Intrati pe site si dati click pe butonul conectare.
            Identificati elementele de tip user si parola si inserati valori incorecte
            (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid).
            Ce tip de testare se aplica aici?
                - Dati click pe butonul "conectare" si verificati urmatoarele:
                        1. Faptul ca nu s-a facut logarea in cont
                        2. Faptul ca se returneaza eroarea corecta

# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida
             (adica fara caracterul "@") si verificati faptul ca butonul "conectare"
             este dezactivat (hint: folositi metoda isEnabled)

Nota:
Daca nu aveti timp sa le faceti pe toate in timpul sesiunii de studiu in echipa le puteti implementa
in oricare din framework-urile de automatizare pe care le veti invata la cursurile viitoare.

Ce tipuri / tehnici de testare ati folosit pentru testele de mai sus? Mai sunt alte teste pe care
le puteti face folosind alte tipuri si tehnici de testare folosite la cursul de testare manuala?

"""

# importam bibliotecile de functii
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializare Chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)



# -----------------------------------------------------------------------------------------------------------------
# Test 1: Intrati pe site-ul https://www.elefant.ro/

chrome.get('https://www.elefant.ro/')
chrome.maximize_window()
sleep(3)
# dam clic ca sa dispara fereastra cu "Allow cookies"...
chrome.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()



# -----------------------------------------------------------------------------------------------------------------
# - Test 2:  Cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
#            cel putin 10 rezultate.   ([class="product-title"])

# cautam un produs...
produs_cautat = 'samsung s23'
chrome.find_element(By.XPATH,'/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/input[1]').click()
sleep(1)
chrome.find_element(By.XPATH,'/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/input[1]').send_keys(produs_cautat)
sleep(1)
chrome.find_element(By.XPATH, '/html/body/header/div[1]/nav/div/div[4]/div/div[1]/form/button/span').click()
sleep(3)

# verificam ca s-au returnat cel putin 10 rezultate...
text_afisat = chrome.find_element(By.XPATH, '/html/body/div[3]/div/div[14]/div[2]/div[2]/div/div[2]/div[2]').text
        # definim o functie for prin care extragem partea numerica din textul afisat ("33 produse")
text_numeric = ''
for i in range(0,(len(text_afisat)-8)):
    text_numeric += text_afisat[i]
numar_produse_gasite = int(text_numeric)
print(f'----------------------------------------------')
print(f"Numar de produse gasite: {numar_produse_gasite}")
        # verificam daca au fost gasite mai mult de 10 produse, adica avem mai mult de 10 rezultate
limita_inferioara = 10
if numar_produse_gasite > limita_inferioara:
    print(f"Au fost gasite mai mult de {limita_inferioara} produse ce corespund criteriului de cautare.")
else:
    print(f"Nu au fost returnate suficiente rezultate in urma cautarii.")



# -----------------------------------------------------------------------------------------------------------------
# - Test 3: Extrageti din lista produsul cu prețul cel mai mic [class="current-price "]
#           (puteti sa va folositi de find_elements)

# sortam lista in ordinea crescatoare a preturilor produselor
chrome.find_element(By.ID, 'SortingAttribute').click()
sleep(1)
chrome.find_element(By.CSS_SELECTOR, '#SortingAttribute > option:nth-child(4)').click()
sleep(1)

nume_produs = chrome.find_element(By.CSS_SELECTOR, '.js-product-tile-031fbd58-da7d-4ddd-bdf2-7bc8d427ab1a > div:nth-child(2) > a:nth-child(3) > h2:nth-child(1)').text
print(f'----------------------------------------------')
print(f'Produsul cu pretul cel mai mic din lista este: ')
print(f'>>> {nume_produs} <<<')
print(f'----------------------------------------------')



# -----------------------------------------------------------------------------------------------------------------
# - Test 4: Extrageti titlul paginii si verificati ca este corect (hint: folositi metoda title)

# se verif ca titlul este ok
chrome.get('https://www.elefant.ro/')
titlu_corect = 'elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!'
titlu_gasit  = chrome.title
try:
    assert titlu_gasit == titlu_corect
    print('Titlul paginii este corect.')
except:
    print('Titlul paginii este incorect.')
    print(f'Cautam ca titlul sa fie >>> {titlu_corect}')



# -----------------------------------------------------------------------------------------------------------------
# - Test 5:  Intrati pe site si dati click pe butonul conectare.
#            Identificati elementele de tip user si parola si inserati valori incorecte
#            (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid).
#            Ce tip de testare se aplica aici?
#                - Dati click pe butonul "conectare" si verificati urmatoarele:
#                        1. Faptul ca nu s-a facut logarea in cont
#                        2. Faptul ca se returneaza eroarea corecta


chrome.get('https://www.elefant.ro/')
# dam clic pe butonul "Conectare" de pe pagina
chrome.find_element(By.CSS_SELECTOR,'.login-prompt').click()
sleep(1)
            # neaparat mereu sa introduci o pauza (sleep...) dupa ce dai clic daca
            # urmeaza sa se deschida o fereastra de dialog
            # ca sa aibe timp serverul sa raspunda si site-ul sa se incarce/actualizeze

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


# verificam daca am ramas pe aceeasi pagina sau am intrat in cont (deci am trecut pe o alta pagina)

        # memoram adresa URL la care suntem inainte de a ne conecta
adresa_curenta = chrome.current_url
        # dam click pe butonul "Conectare"
chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button').click()
sleep(1)
        # memoram adresa URL la care suntem dupa ce am dat clic
adresa_dupa_click_conectare = chrome.current_url
        # verificam daca suntem pe aceeasi pagina
if adresa_curenta == adresa_dupa_click_conectare:
    print(f'Am ramas pe aceeasi pagina de site. Deci nu s-a facut logarea pe cont.')
else:
    print(f'Am plecat de pe pagina respectiva. Deci m-am logat pe cont.')


# verificam faptul ca nu s-a facut logarea pe cont
# ?????????????????????? ?????????? ?????????

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
# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida    (adica fara caracterul "@")
#           si verificati faptul ca butonul "conectare" este dezactivat. (hint: folositi metoda isEnabled)

chrome.find_element(By.CSS_SELECTOR, '#ShopLoginForm_Login').clear()
chrome.find_element(By.CSS_SELECTOR, '#ShopLoginForm_Login').send_keys('Portocale_albastre')
sleep(1)
codul_elementului = chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[9]/div[1]/div/div[1]/div/form/div[4]/div/button').get_attribute('outerHTML')
marcaj_dezactivare = 'disabled="disabled"'
if marcaj_dezactivare in codul_elementului:
    print (f'Butonul "Conectare" este dezactivat.')
else:
    print(f'Butonul "Conectare" este activat.')