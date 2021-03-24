from django.http import HttpResponse, response
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from discount.views import work_discount

import time
import unittest


from selenium.webdriver.support import ui

MAX_WAIT = 4


class NewVisitorTest(TestCase):

    # automatically start a page
    def setUp(self):
        chromedriver = './chromedriver'
        self.browser = webdriver.Chrome(chromedriver)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='YYLRPL', password='qazokm123')

    # automatically close a page when test finished
    def tearDown(self):
        self.browser.quit()

    # the browser has been opened for twice?
    # 頁面開了兩次 安捏乾丟？還是functional test我應該放在同一個def 不拆開寫？
    def test_from_home_page(self):
        self.browser.get('http://127.0.0.1:8000/')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('milet desu', header_text)

    def test_about_page_template(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'about.html')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_template(self):
        response = self.client.get('/contact')
        self.assertTemplateUsed(response, 'contact.html')
        self.assertEqual(response.status_code, 200)

    def test_anonymous_user_log_in(self):
        # self.browser.get('http://127.0.0.1:8000/account/login')
        # name_inputbox = self.browser.find_element_by_xpath('//*[@id="id_username"]')
        # name_inputbox.send_keys('YYLRPL')
        # name_inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)
        # password_inputbox = self.browser.find_element_by_id('//*[@id="id_password"]')
        # password_inputbox.send_keys('qazokm123')
        # password_inputbox.send_keys(Keys.ENTER)
        # time.sleep(4)
        pass

    # if anonymous user can only see 10 items in work_discount page
    def test_anonymous_user_in_work_discount_page(self):
        request = self.factory.get('/work_discount')
        request.user = AnonymousUser()
        response = work_discount(request)
        self.assertEqual(response.status_code, 200)

    # # if user can see 10+ items & card, extra discount in work_discount page
    def test_authentic_user_in_work_discount_page(self):
        request = self.factory.get('/work_discount')
        request.user = self.user
        response = work_discount(request)
        # self.assertIn(response.content.decode('Card'))
        # self.assertIn(response.content.decode(), '<th>Card</th>')
        # self.assertIn(response.content.decode(), '<th>Cash Back</th>')
        self.assertIn('Card', response.content.decode())
        self.assertIn('Cash Back', response.content.decode())
        self.assertEqual(response.status_code, 200)

    # user log out
    def test_authentic_user_log_out(self):
        pass


if __name__ == '__main__':
    unittest.main(warnings='ignore')