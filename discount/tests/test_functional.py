from django.test import TestCase
from selenium import webdriver
# from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import unittest

MAX_WAIT = 4


class NewVisitorTest(unittest.TestCase):

    # automatically start a page
    def setUp(self):
        chromedriver = './chromedriver'
        self.browser = webdriver.Chrome(chromedriver)

    # automatically close a page when test finished
    def tearDown(self):
        self.browser.quit()

    def test_from_home_page(self):
        self.browser.get('http://127.0.0.1:8000/')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('milet desu', header_text)



# if __name__ == '__main__':
#     unittest.main(warnings='ignore')