from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://the-internet.herokuapp.com/redirector')

chrome.maximize_window()
sleep(3)

# În codul HTML se găseşte sub forma:
# <a href='link_de_redirectionare'>text care este pus peste link</a>
# unde:
# 'a' este prescurtare de la 'ancoră' şi este legătura către alt link
# 'href' este prescurtare de la 'hipertextreferrence' şi reprezintă pagina către care se va naviga
# atunci când se va da click pe acel link.


# Selectorul LINK_TEXT
# click_on_me = chrome.find_element(By.LINK_TEXT, 'here')
# click_on_me.click()
# sleep(2)
#
# chrome.find_element(By.LINK_TEXT, '200').click()
# sleep(2)


# Exercitiu cu URL greşit ca să vedem cum este afişată eroarea în consolă.
# chrome.find_element(By.LINK_TEXT, 'here').click()
# assert chrome.current_url == 'https://the-internet.herokuapp.com/status_codes', 'Error, URL-ul nu este corect.'

# Selector Partial Link Text - este o alternativă pentru selectorul LINK_TEXT atunci când
# textul este prea lung sau se schimbă frecvent

# link_partial = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Elemental')
# sleep(2)
# link_partial.click()
# sleep(2)

try:
    chrome.find_element(By.PARTIAL_LINK_TEXT, 'he').click()
    assert chrome.current_url == 'https://the-internet.herokuapp.com/status_codes', 'Error: URL is not correct!'
    print("Current URL is correct.")
except AssertionError as e:
    print(e)

