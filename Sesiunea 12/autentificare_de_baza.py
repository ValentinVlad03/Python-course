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

class Autentification(TestCase):
    USER = 'admin'
    PAROLA = 'admin'

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/basic_auth')

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_auth(self):
        expected_text = "Congratulations! You must have the proper credentials."
        self.chrome.get('https://' + self.USER + ':' + self.PAROLA + '@the-internet.herokuapp.com/basic_auth')
        sleep(3)
        actual_text= WebDriverWait(self.chrome, 3).until(EC.text_to_be_present_in_element((By.ID, 'content'),
                                                     "Congratulations! You must have the proper credentials."))
        self.assertTrue(expected_text, actual_text)
        print("Assert True a fost corect.")

