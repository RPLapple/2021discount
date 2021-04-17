from django.test import TestCase
from selenium import webdriver

import time

MAX_WAIT = 4


class NewVisitorTest(TestCase):

    # automatically start a page
    def setUp(self):
        chromedriver = './chromedriver'
        self.browser = webdriver.Chrome(chromedriver)

    # automatically close a page when test finished
    def tearDown(self):
        self.browser.quit()

    # the browser has been opened for twice?
    def test_from_home_page(self):
        self.browser.get('http://127.0.0.1:8000/')
        time.sleep(1)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('We', header_text)

    # if anonymous user can only see 10 items in work_discount page
    def test_anonymous_user_in_work_discount_page(self):
        self.browser.get('http://127.0.0.1:8000/work_discount')
        text = self.browser.find_element_by_id('more').text
        self.assertIn('more', text)

    # Auth user can see 10+ items & card, extra discount in work_discount page
    def test_authentic_user_in_work_discount_page(self):
        pass