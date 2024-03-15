# - Test 1: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
# - Test 2: faceti filtrare dupa pret si verificati faptul ca toate produsele returnate au pretul in intervalul de filtrare
# - Test 3: Cautati un produs care nu exista si verifica faptul ca mesajul returnat este: "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."
# - Test 4: Cautati un produs, sortati lista de rezultate in ordine crescatoare dupa pret si verificati faptul ca produsele au fost intr-adevar sortate
# - Test 5: Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare dupa pret si verifica faptul ca produsele au fost intr-adevar sortate
# - Test 6: Intrati pe elefant.ro, dati click pe linkul Contact, si verificati faptul ca nu puteti sa dati submit la formular daca nu sunt completate campurile obligatorii (verificati ca ramaneti pe aceeasi pagina) (hint: folositi metoda current_url)

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()
chrome.get("https://www.elefant.ro/")
cookies_accept = WebDriverWait(chrome, 10).until(
    EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookies_accept.click()
sleep(2)



# - Test 1: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat
# cel putin 10 rezultate ([class="product-title"])

search_box = chrome.find_element(By.XPATH, '//div[@class="row"]//input[@name="SearchTerm"]')
search_box.click()
search_box.send_keys("iphone 14")
sleep(2)
click_search = chrome.find_element(By.XPATH, '//div[@id="HeaderRow"]//div[@class="row"]//button')
click_search.click()
sleep(2)
# a.varianta in care ne folosim de functia Keys.RETURN care simuleaza tasta "Enter"
search_box.send_keys(Keys.RETURN)
sleep(2)
# b. sau varianta in care ne folosim de metoda submit deoarece formularul de tip input (de pe pagina elefant) are un buton
# de tip "submit" (<button class="btn-search btn btn-primary" type="submit" name="search" title="Începe căutarea">)
search_box.submit()
sleep(2)
product_result = chrome.find_elements(By.CSS_SELECTOR, '.product-title')
assert len(product_result) >= 10, "Error, the search did not return enough results"
sleep(2)



# - Test 3: Cautati un produs care nu exista si verifica faptul ca mesajul returnat este:
# "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."

search_box = chrome.find_element(By.XPATH, '//div[@class="row"]//input[@name="SearchTerm"]')
search_box.click()
search_box.send_keys("cfssjoweral")
sleep(2)
click_search = chrome.find_element(By.XPATH, '//div[@id="HeaderRow"]//div[@class="row"]//button')
click_search.click()
sleep(2)
error_message = chrome.find_element(By.XPATH, '//div[@class = "no-search-result"]')
error = error_message.text
expected_error = 'NU A FOST GĂSIT NICI UN REZULTAT :'
assert expected_error in error, f"Error message is wrong. We got {error}"



# - Test 4: Cautati un produs, sortati lista de rezultate in ordine crescatoare dupa pret si verificati
# faptul ca produsele au fost intr-adevar sortate

search_box = chrome.find_element(By.XPATH, '//div[@class="row"]//input[@name="SearchTerm"]')
search_box.click()
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
dropdown_list = Select(chrome.find_element(By.ID,"SortingAttribute")) # am instantiat un obiect din clasa Select
dropdown_list.select_by_visible_text("Pret crescator")
sorted_product_prices_ascending = chrome.find_elements(By.CSS_SELECTOR, '.current-price')
# #pentru ca am constat ca unele produse au N/A a trebuit sa pun un filtru in plus si pt aceasta categorie
filtered_prices = [price.text for price in sorted_product_prices_ascending if price.text != 'N/A']
# #extragem textul din fiecare element din lista si inlocuim virgula cu punct pt a face un format numeric corect
prices_ascending = [float(price.replace(",", ".")) for price in filtered_prices]
# #ma folosesc de functia sorted() ca sa sortez elementele listei. Functia sorteaza crescator by default
assert prices_ascending == sorted(prices_ascending), ("Products are not asc sorted")



# - Test 5: Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare dupa pret
# si verifica faptul ca produsele au fost intr-adevar sortate

search_box = chrome.find_element(By.XPATH, '//div[@class="row"]//input[@name="SearchTerm"]')
search_box.click()
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
dropdown_list = Select(chrome.find_element(By.ID,"SortingAttribute")) # am instantiat un obiect din clasa Select
dropdown_list.select_by_visible_text("Pret descrescator")
sorted_product_prices_descending = chrome.find_elements(By.CSS_SELECTOR, '.current-price')
filtered_prices = [price.text for price in sorted_product_prices_descending if price.text != 'N/A']
# #pentru ca am constat ca avem si preturi (9.824.73 lei) care nu pot fi facute ca fiind float a trebuit a fac urmatoarele
# #am inlocuit virgula si punctele din preturi cu nimic :) si le-am salvat in lista mea
filtered_prices_cleaned = [price.replace(",", "").replace(".", "") for price in filtered_prices]
# #am convertit preturile filtrate si curatate de lei, virgula si puncte in format float
prices_descending_filtered = [float(price.replace(" lei", "")) if price != 'N/A'
                              else 0.0 for price in filtered_prices_cleaned]
# #am convertit toate preturile nefiltrate in numere float. Am mai adaugat clauza ca in cazul in care sunt
# # produse cu N/A sa imi inlocuiasca cu valoarea 0.0, asta pt a depasi erorile care apareau la rularea codului
prices_descending = [float(price.text.replace(",", "").replace(".", "").replace
                           (" lei", "")) if price.text != 'N/A' else 0.0 for price in
                     sorted_product_prices_descending]
# #folosesc aceast functie sorted dar ii dau argumentul reverse=True pt a face sortarea descarescatoare
assert prices_descending == sorted(prices_descending, reverse=True), "Products are not desc sorted"



# - Test 6: Intrati pe elefant.ro, dati click pe linkul Contact, si verificati faptul ca nu puteti sa dati submit
# la formular daca nu sunt completate campurile obligatorii (verificati ca ramaneti pe aceeasi pagina)
# (hint: folositi metoda current_url)

chrome.get("https://www.elefant.ro/")
cookies_accept = WebDriverWait(chrome, 10).until(
    EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookies_accept.click()
sleep(2)
chrome.find_element(By.LINK_TEXT, "Contact").click()
submit_button = chrome.find_element(By.XPATH, '//div[@class="o-btn o-btn-send"]')
submit_button.click()
assert chrome.current_url == "https://www.elefant.ro/helpdesk/contact-us", "Error : page is not correct"

