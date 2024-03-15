from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# pentru Firefox (Mozilla):     from webdriver_manager.firefox import GeckoDriverManager
# pentru Edge :                 from webdriver_manager.microsoft import EdgeChromiumDriverManager
# pentru Safari:                from webdriver_manager.safari import SafariDriverManager
# pentru Opera:                 from webdriver_manager.opera import OperaDriverManager

from selenium.webdriver.common.by import By

# initializare Chrome

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# in cazul in care folositi o versiune mai veche de PyCharm va trebui sa va setati descarcarea
# driverului corect in mod dinamic. Puteti face asta prin comanda de mai jos:
#      chrome = webdriver.Chrome(executable_patch = ChromeDriverManager().install())

# navigam catre un URL
# chrome.get('https://formy-project.herokuapp.com/')

# maximizarea ferestrei (browserului, cea deschisa prin rularea codului)
# chrome.maximize_window()
# sleep(5)

# inchiderea instantei de Chrome se face cu comanda de mai jos!
# Se va folosi după ce am inserat toate testele dorite.
# chrome.quit()

# pentru inchiderea unui tab din Chrome folosesti comanda
# chrome.close()

# ----------------------------------------------

# Selector ID
# cautarea
chrome.get('https://formy-project.herokuapp.com/form')

# first_name = chrome.find_element(By.ID, 'first-name')
# sleep(1)
# first_name.send_keys('Lidia')
# sleep(2)
#
# last_name = chrome.find_element(By.ID, 'last-name')
# sleep(1)
# last_name.send_keys('Popa')
# sleep(2)


# mai jos e metoda recomandata pentru economisirea de cod
# chrome.find_element(By.ID, 'last-name').send_keys('Popa')
# sleep(2)

# Modelul pe care îl veţi folosi în testare
try:
    first_name = chrome.find_element(By.ID,  'first-name')
    first_name.send_keys('Lidia')
    sleep(2)
except:
    print('ID-ul nu este corect.')
print('Am reusit cu succes.')