import unittest
from unittest import TestCase
from HtmlTestRunner.runner import HTMLTestRunner
# import HTMLTestRunner

from Sesiunea12.alerte import Alerts
from Sesiunea12.imitand_tastatura import Keyboard
from Sesiunea12.context_menu import ContextMeniu
from Sesiunea12.autentificare_de_baza import Autentification
from Sesiunea12.edge import Browser

class TestSuite(unittest.TestCase):

    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMeniu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Autentification),
            unittest.defaultTestLoader.loadTestsFromTestCase(Browser)
        ])
        runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='Raportul nr. x',
                                open_in_browser=True, description='HTMLTestReport', tested_by='Valentin')
        runner.run(teste_de_rulat)