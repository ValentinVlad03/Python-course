# - Test 1: Intrati pe site-ul https://www.elefant.ro/
# - Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
# - Test 3: Extrageti din lista produsul cu prețul cel mai mic [class="current-price "] (puteti sa va folositi de find_elements)
# - Test 4: Extrageti titlul paginii si verificati ca este corect (hint: folositi metoda title)
# - Test 5: Intrati pe site si dati click pe butonul conectare.
# Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid). Ce tip de testare se aplica aici?
# - Dati click pe butonul "conectare" si verificati urmatoarele:
#             1. Faptul ca nu s-a facut logarea in cont
#             2. Faptul ca se returneaza eroarea corecta
# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat (hint: folositi metoda isEnabled)

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()
#
# # - Test 1: Intrati pe site-ul https://www.elefant.ro/
chrome.get("https://www.elefant.ro/")
cookies_accept = WebDriverWait(chrome, 10).until(
    EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookies_accept.click()
sleep(2)
#
# # - Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
search_box = chrome.find_element(By.XPATH, '//div[@class="row"]//input[@name="SearchTerm"]')
search_box.click()
search_box.send_keys("iphone 14")
sleep(2)
click_search = chrome.find_element(By.XPATH, '//div[@id="HeaderRow"]//div[@class="row"]//button')
click_search.click()
sleep(2)
# a.varianta in care ne folosim de functia Keys.RETURN care simuleaza tasta "Enter"
# search_box.send_keys(Keys.RETURN)
# sleep(2)
# b. sau varianta in care ne folosim de metoda submit deoarece formularul de tip input (de pe pagina elefant) are un buton
# de tip "submit" (<button class="btn-search btn btn-primary" type="submit" name="search" title="Începe căutarea">)
# search_box.submit()
# sleep(2)
product_result = chrome.find_elements(By.CSS_SELECTOR, '.product-title')
assert len(product_result) >= 10, "Error, the search did not return enough results"
sleep(2)
#
# # # - Test 3: Extrageti din lista produsul cu prețul cel mai mic [class="current-price "] (puteti sa va folositi de find_elements)
price_list = chrome.find_elements(By.CSS_SELECTOR, '.current-price')
    #initializam doua variabile pt pretul minim si produsul cu pret minim
minim_price = None  # variabila care va tine evidenta pretului minim. Am pus None pt ca in aceasta faza nu am
                    # identificat niciun pret (adica indicam lipsa unei valori), adica nu ii dam o valoare initiala
product_with_minim_price = None #variabila care va tine evidenta produselor cu pretul minim

    #iteram prin fiecare element pt a gasi pretul minim
for e in price_list: #scriem o bucla for pt a itinera in lista de preturi
    price_text = e.text.replace(" lei", "").replace(",", ".")
    #extragem textul din fiecare element din lista si, eliminam cuvantul lei si inlocuim virgula cu punct pt a face un
    # format numeric corect

    #convertim textul intr-un nr
    try:
        price = float(price_text) # convertim textul intr-un nr float si il stocam in variabila price
    except ValueError:
        print(f"Attention!! Current {price_text} can't be converted")

    if minim_price is None or (price is not None and price < minim_price): #verificam daca pretul minim nu a fost
        # setat deja si daca este un nr valid
        minim_price = price
        product_with_minim_price = e

    #verificam daca am gasit un pret minim si afisam
if product_with_minim_price is not None: #verificam daca s-a gasit un pret minim valid
    print(f"Product with mimim price is : {product_with_minim_price.text}")
    print(f"Minim price is : {minim_price} lei")
else:
    print("Price are not valide")

# # - Test 4: Extrageti titlul paginii si verificati ca este corect (hint: folositi metoda title)
page_title = chrome.title
# print(page_title)
assert "Vino pe Elefant.ro!" in page_title, f"Page title is incorrect"


# - Test 5: Intrati pe site si dati click pe butonul conectare.

chrome.get("https://www.elefant.ro/")
cookies_accept = WebDriverWait(chrome, 10).until(
    EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookies_accept.click()
sleep(2)

chrome.find_element(By.CLASS_NAME,"my-account-link").click()
connect_button = chrome.find_element(By.XPATH, '//div[@id="account-layer"]//a[contains(text(),"Conectare")]')
# mai jos am folosit clasa ActionChains ca sa putem sa interactionam cu un element de tip context menu
# cu care nu putem interactiona asa cum o facem cu elementele standard
ActionChains(chrome).move_to_element(connect_button).click(connect_button).perform()
chrome.find_element(By.ID,"ShopLoginForm_Login").send_keys("alabala@gmail.com")
chrome.find_element(By.ID, "ShopLoginForm_Password").send_keys("testpassword")
chrome.find_element(By.XPATH,'//button[@value="Login"]').click()
# verificare a faptului ca nu ne-am logat -> prin intermediul url-ului
expected_url = "https://www.elefant.ro/INTERSHOP/web/WFS/elefant-elefantRO-Site/ro_RO/-/RON/ViewUserAccount-ProcessLogin"
actual_url = chrome.current_url
assert expected_url == actual_url,"Error: Maybe you should check the login functionality"
message = chrome.find_element(By.XPATH, '//div[@class ="alert alert-danger"]').text
error_message = message
expected_message = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
assert error_message == expected_message, f"Wrong alert"

# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat (hint: folositi metoda isEnabled)
chrome.get("https://www.elefant.ro/")
cookies_accept = WebDriverWait(chrome, 10).until(
    EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookies_accept.click()
sleep(2)

chrome.find_element(By.CLASS_NAME,"my-account-link").click()
connect_button = chrome.find_element(By.XPATH, '//div[@id="account-layer"]//a[contains(text(),"Conectare")]')
# mai jos am folosit clasa ActionChains ca sa putem sa interactionam cu un element de tip context menu
# cu care nu putem interactiona asa cum o facem cu elementele standard
ActionChains(chrome).move_to_element(connect_button).click(connect_button).perform()
user = chrome.find_element(By.ID,"ShopLoginForm_Login")
user.send_keys("alabala@gmail.com")
user.clear()
user.send_keys("gmail.com")
log_in = chrome.find_element(By.XPATH,'//button[@value="Login"]')
assert not log_in.is_enabled()










