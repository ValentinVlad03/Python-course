from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://the-internet.herokuapp.com/login')

# Selector Name - se poate face căutare în web folosind: [name = 'valoareName']

# username = chrome.find_element(By.NAME, 'username')
# sleep(2)
# username.send_keys("tomsmith")
# sleep(2)
#
# password = chrome.find_element(By.NAME, "password")
# sleep(2)
# password.send_keys("SuperSecretPassword!")
# sleep(2)
#
# login_button = chrome.find_element(By.CLASS_NAME, 'radius')
# login_button.click()
# sleep(2)


# Exemplu:  atunci când introduci parola greşită.
username = chrome.find_element(By.NAME, 'username')
username.send_keys("tomsmith")
password = chrome.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword")
login_button = chrome.find_element(By.CLASS_NAME, 'radius')
login_button.click()
error_code_locator = chrome.find_element(By.ID, 'flash')

try:
    asteptare_eroare = WebDriverWait(chrome, 10).until(EC.visibility_of(error_code_locator))
    assert asteptare_eroare.is_displayed()
    print("Mesajul de eroare este afişat.")
    sleep(3)
except AssertionError:
    print("Elementul cu ID 'flash' nu este vizibil.")
