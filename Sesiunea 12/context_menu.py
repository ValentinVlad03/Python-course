from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

class ContextMeniu(TestCase):
    BOX = (By.ID, "hot-spot")

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/context_menu')


    def tearDown(self) -> None:
        self.chrome.quit()

    def test_context(self):
            # initializam obiectul ActionChain pentru a simula actiuni de mouse (actiunea de click dreapta) ca sa dam click dreapta.
        action = ActionChains(self.chrome)
            # identificam elementul asupra caruia se va efectua click dreapta
        element = self.chrome.find_element(*self.BOX)
            # executam actiunea de click dreapta pe elementul identificat
        action.context_click(element).perform()
        sleep(3)
        self.chrome.switch_to.alert.accept()
        sleep(3)