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

    # the browser has been opened for twice?
    # 頁面開了兩次 安捏乾丟？還是functional test我應該放在同一個def 不拆開寫？
    def test_from_home_page(self):
        self.browser.get('http://127.0.0.1:8000/')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('milet desu', header_text)

    def test_AnonymousUser_in_work_discount_page(self):
        self.browser.get('http://127.0.0.1:8000/work_discount')
        # only show 10 items 是否只show 10樣東西
        # loggin 登入會員
        # back to same page and should present cards and extra discount 再回到該頁面，是否有顯示卡名和特特惠


if __name__ == '__main__':
    unittest.main(warnings='ignore')