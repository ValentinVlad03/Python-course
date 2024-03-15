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
#
# chrome.get('https://formy-project.herokuapp.com/scroll')
#
# chrome.maximize_window()
# sleep(3)
#
# """
# Căutarea în pagina web pentru CSS selector se poate face:
# --- Selectarea după ID se face cu = #myID
# --- Selectarea după clasă = .myClass
# --- Selectarea după tipul de element = input
# --- Căutarea primului copil a unui element se poate face folosind caracterul '>' sau cu sintaxa first-of-type
# --- Căutarea ultimului copil al unui element se face cu sintaxa last-of-type
# --- Căutarea unui copil care nu este nici primul nici ultimul. In acest caz se foloseşte nth-of-type
#
# """
#
# chrome.find_element(By.CSS_SELECTOR, 'input#name').send_keys('Cristina')    # am căutat după ID
# sleep(2)
#
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys(' Dumitru')     # am căutat după clasă
# sleep(2)
#
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder = "MM/DD/YYYY"]').send_keys('14/12/2023')    # am căutat după placeholder
# sleep(2)
#
# chrome.find_element(By.ID, 'logo').click()
# sleep(2)
#
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Web Form').click()
# sleep(2)
#
# chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder *= "first name"]').send_keys('Cristina')
#         # folosim *=  pentru a ne scrie tot conţinutul placeholder-ului
#         #   *=   înseamnă 'conţine'
# sleep(2)
#
# chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder *= "last name"]').send_keys('Dumitru')
# sleep(2)
#
# # Exercitiu:  am făcut navigare din părinte în copil combinată cu căutare după tip atribut-valoare
# text_label_name = chrome.find_element(By.CSS_SELECTOR, 'strong > label[for="last-name"]').text
# text_afisat_pe_web = text_label_name
# textul_asteptat = ('Last name')
#
# try:
#     assert text_afisat_pe_web == textul_asteptat
#     print("Titlul căsuţei este corect: '{}' ".format(text_afisat_pe_web))
# except AssertionError:
#     print("Mesajul este greşit. Aşteptat {}. Actual {}.".format(textul_asteptat, text_afisat_pe_web))
#
#
# # cautare dupa primmul copil de tip div a unui div identificat dupa clasa (clasa de tip input-group)
# education_label = chrome.find_element(By.CSS_SELECTOR, 'div.input-group>div:first-of-type label').text
# # cautarea dupa primul copil se face cu first-of-type
#
#
# # cautare dupa al doilea copil de tip div al unui div cu clasa input-group
# chrome.find_element(By.CSS_SELECTOR, 'div.input-group>div:nth-of-type(2)').click()
#
# # in cazul in care se face cautarea dupa un copil care nu este nici primul nici ultimul se foloseste nth-of-type
#
# # cautare dupa ultimul copil de tip div al unui div cu clasa input-group
# chrome.find_element(By.CSS_SELECTOR, 'div.input-group>div:last-of-type input').click()
#
# # cautare dupa un element de tip input care are ca si frate un element de tip strong
# # (mai intai am identificat parintele de tip div, apoi copilul de tip div care continea la randul lui,
# # copilul de tip strong).
# chrome.find_element(By.CSS_SELECTOR, 'div.form-group > div:nth-of-type(2) > strong + input').send_keys("test")


# cautare in liste (elemente de tip DropDown)
# chrome.get('https://www.ebay.com/')
# chrome.maximize_window()
#
# ebay = Select(chrome.find_element(By.ID, 'gh-cat'))
# ebay.select_by_visible_text("Antiques")
# sleep(5)

# find_elements = se utilizeaza atunci cand vrem sa aducem lista intreaga de elemente de un anumit tip
chrome.get('https://formy-project.herokuapp.com')
lista_elemente = chrome.find_elements(By.TAG_NAME,'div')
print(len(lista_elemente))