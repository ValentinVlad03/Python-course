# from time import sleep
# from selenium import webdriver
# from selenium.webdriver import Keys
# # from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# # from webdriver_manager.chrome import ChromeDriverManager
# import unittest
# from selenium.webdriver.support import expected_conditions as EC
# from unittest import TestCase
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# class Browser(TestCase):
#
#     def setUp(self) -> None:
#         s = Service(EdgeChromiumDriverManager().install())
#         self.edge = webdriver.Edge(service=s)
#         self.edge.maximize_window()
#         self.edge.get('https://formy-project.herokuapp.com/form')
#
#     def tearDown(self) -> None:
#         self.edge.quit()
#
#     def test_edge(self):
#         first_name = self.edge.find_element(By.ID, "first-name")
#         first_name.send_keys("Lidia ne invata meserie")
#

from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# import unittest
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class Browser(TestCase):

    def setUp(self) -> None:
        self.edge = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.edge.maximize_window()
        self.edge.get('https://formy-project.herokuapp.com/form')

    def tearDown(self) -> None:
        self.edge.quit()

    def test_edge(self):
        first_name = self.edge.find_element(By.ID, "first-name")
        first_name.send_keys("Lidia ne invata meserie")
        sleep(1)
        last_name = self.edge.find_element(By.ID, 'last-name')
        last_name.send_keys("iar noi practicam sarguincios")
        sleep(1)
        job_title = self.edge.find_element(By.ID, 'job-title')
        job_title.send_keys("Tester software")
        sleep(1)
        # Selectez apoi butonul "college"
        self.edge.find_element(By.ID, 'radio-button-2').click()
        sleep(1)
        # Sex - optiunea Male
        self.edge.find_element(By.ID, 'checkbox-1').click()
        sleep(1)
        # la "Years of experience" selectăm opţiunea "0-1"
        self.edge.find_element(By.ID, 'select-menu').click()
        sleep(1)
        self.edge.find_element(By.XPATH, '/html/body/div/form/div/div[6]/select/option[2]').click()
        sleep(1)
        # apoi punem data curenta, adica 24 ianuarie 2024
        self.edge.find_element(By.ID, 'datepicker').click()
        sleep(1)
        self.edge.find_element(By.XPATH, '/html/body/div[2]/div[1]/table/tbody/tr[4]/td[4]').click()
        sleep(1)
        self.edge.find_element(By.CSS_SELECTOR, '.btn').click()
        sleep(4)

