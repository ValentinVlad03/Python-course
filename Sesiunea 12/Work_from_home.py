from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

class Keyboard(TestCase):
    USER = (By.ID, "username")
    PASSWORD = (By.ID, "password")


    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/login')


    def test_select_all(self):
        utilizator = self.chrome.find_element(*self.USER)
        # utilizator.send_keys("Lidia Popa")
        # sleep(2)
        # utilizator.clear()    # metoda "Clear" este folosita pentru a sterge tot continutul din textbox.
        # sleep(2)
        # utilizator.send_keys("Lidia Popa 2")
        # sleep(1)
        # # ne folosim de clasa keys (clasa furnizata de Selenium). Clasa Keys contine functii care simuleaza actiunile de la tastatura.
        # utilizator.send_keys(Keys.CONTROL, 'a')  # omolog cu tastele CTRL + A, adica "select all".
        # sleep(1)
        # utilizator.send_keys(Keys.BACKSPACE)   # simuleaza stergerea de la tastatura
        # sleep(1)
        # utilizator.send_keys("Lidia Popaaaa")
        # sleep(1)
        # utilizator.send_keys(Keys.ARROW_LEFT)   # simuleaza apasarea tastei cu sageata la stanga
        # sleep(2)
        utilizator.clear()
        utilizator.send_keys("tomsmith")
        sleep(2)

        parola = self.chrome.find_element(*self.PASSWORD)
        parola.send_keys("abracadabra")
        sleep(2)
        parola.send_keys(Keys.CONTROL, 'a')
        parola.send_keys(Keys.BACKSPACE)
        parola.send_keys("SuperSecretPassword!")
        sleep(2)
        print(f"Am introdus parola corecta.")
        self.chrome.find_element(By.CSS_SELECTOR, '.radius').click()
        sleep(4)


    # def test_backspace_for(self):
    #     user = self.chrome.find_element(*self.USER)
    #     user.send_keys('a', 'b', 'c', 'd', 'e', 'f')
    #     sleep(3)
    #     for i in range(0,5):
    #         user.send_keys(Keys.BACKSPACE)
    #         print(f'Am sters {i} litera.')
    #         sleep(1)
    #         i += 1
    #     sleep(2)


    def tearDown(self) -> None:
        self.chrome.quit()