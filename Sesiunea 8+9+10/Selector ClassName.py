from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

# initializare Chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizarea ferestrei (browserului, cea deschisa prin rularea codului)
chrome.maximize_window()

# Selector ClassName = este bazat pe clase
chrome.get('https://formy-project.herokuapp.com/')
# clasa_mea = chrome.find_element(By.CLASS_NAME, 'nav-link')
# sleep(2)
# clasa_mea.click()
# sleep(2)


# ex. 2
# chrome.find_element(By.CLASS_NAME, 'nav-link').click()
# sleep(2)


# ex. 3
element_web = chrome.find_element(By.CLASS_NAME, 'lead')
textul_de_pe_element = element_web.text

expected_text = "This is a simple site that has form components that can be used for testing purposes."

try:
    assert textul_de_pe_element == expected_text
    print("Mesajul este corect: '{}'".format(textul_de_pe_element))
except AssertionError:
    print("Mesajul este greşit. Asteptat: {}. Actual: {}".format(expected_text, textul_de_pe_element))
