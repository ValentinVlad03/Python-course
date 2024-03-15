"""
1. Pentru a putea folosi această librărie va trebui să creăm clase de test care să o moştenească.

import unittest         # modulul unittest face parte din biblioteca Python standard şi furnizează un framework
                        pentru testare unitară şi automată.

class MyTest(unittest.TestCase)
                        # unittest.TestCase este clasa de bază pe care o vom extinde cu diferite teste.

    def testeaza_ceva(self)
        ...cod de testare...

Atunci când ne folosim de librăria unittest, clasa de bază va trebui să conţină şi următoarele componente:
a) setup - care conţine instrucţiuni ce trebuie să fie executate de fiecare test (precondiţii)
b) teardown - care conţine instrucţiuni ce trebuie să fie executate după fiecare test.


exemplu:
class MyTest(unittest.TestCase):
    def setUp(self)
        # pregătirea resurselor pentru teste
        pass

    def tearDown(self):
        # curăţarea resurselor după test
        pass

    def testeaza_ceva(self):
        # cod de testare

Fiecare clasă de test trebuie să înceapă obligatoriu cu prefixul   test_  ca să poată fi recunoscută de pachetul pytest.
Orice metodă va trebui să se termine cu o instrucţiune de assert.
Unittest furnizează o serie de metode de assert pe care le putem folosi, cum ar fi:  assertEqual, assertTrue, assertIn, etc.

Ex.
class MyTest(unittest.TestCase):
    def testeaza_ceva(self):
        x = 1
        self.assertEqual(x, 1, "x nu este 1")


Atunci când vrem să sărim unele teste la rulare ne putem folosi de decoratorul   @unittest.skip  plasat întotdeauna
înainte fiecărei metode de test pe care dorim să o sărim.


class MyTest(unittest.TestCase):

    @unittest.skip                      # acest test va fi sărit
    def test_testeaza_ceva(self):
        x = 1
        self.assertEqual(x, 1, "x nu este 1")

    def test_altceva(self):             # acest test va fi executat
        pass

Executarea testelor:
click pe triunghiul verde de langa numele clasei >>> va rula toate testele din acea clasa
click pe triunghiul verde de langa numele metodei >>> va rula doar metoda respectiva
rularea din terminal a unui fisier specific de teste :  python -m filename.py
rularea din terminal a tuturor fisierelor de test : python -m unittest


"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):
    # Aici definim constantele care să stocheze valoarea de căutare a selectorului pe care îl căutăm.
    # Pentru a indica că o variabilă trebuie tratată ca şi constantă, se folosesc majuscule în denumirea lor.
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    JOB_TITLE_INPUT = (By.ID, 'job-title')
    HIGH_SCHOOL_BTN = (By.ID, 'radio-button-1')
    MALE_CHECK_BOX = (By.ID, 'checkbox-1')
    YEARS_OF_EXP_0_1 = (By.XPATH, "//*[@id = 'select-menu']/option[2]")
    DATE_SELECT = (By.ID, 'datepicker')
    SUBMIT_BTN = (By.XPATH, "//a[@role = 'button']")


    def setUp(self) -> None:    # -> None  înseamnă că această funcţie nu returnează nimic explicit.
                                # Funcţiile de configurare cum ar fi setUp şi tearDown sunt adesea definite să nu
                                # returneze nimic.

        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://formy-project.herokuapp.com/form')

    def tearDown(self) -> None:
        self.chrome.quit()

    @unittest.skip
    def test_check_url(self):
        actual = self.chrome.current_url
        expected = 'https://formy-project.herokuapp.com/form'
        self.assertEqual(actual, expected, 'The page is not correct')
        sleep(2)

    def test_form(self):
        input_first_name = self.chrome.find_element(*self.FIRST_NAME_INPUT)
        input_first_name.send_keys('Lidia')
        self.assertTrue(input_first_name.is_displayed(), 'Mesajul afisat este corect.')
        sleep(2)
        self.chrome.find_element(*self.LAST_NAME_INPUT).send_keys('Popa')
        sleep(2)
        self.chrome.find_element(*self.JOB_TITLE_INPUT).send_keys('Tester')
        sleep(2)
        self.chrome.find_element(*self.HIGH_SCHOOL_BTN).click()
        sleep(2)
        self.chrome.find_element(*self.MALE_CHECK_BOX).click()
        sleep(2)
        self.chrome.find_element(*self.YEARS_OF_EXP_0_1).click()
        sleep(2)
        self.chrome.find_element(*self.DATE_SELECT).click()
        sleep(2)
        self.chrome.get_screenshot_as_file('ss_pagina.png')

    def test_submit_button(self):
        self.chrome.find_element(*self.SUBMIT_BTN).click()
        actual = WebDriverWait(self.chrome, 5).until(EC.text_to_be_present_in_element(By.XPATH,
                                                                                      '/html/body/div/div'),
                                                     "The form was succesfully submitted!")
        if actual:
            print("Message found is correct.")
        else:
            print("Message found is incorrect.")