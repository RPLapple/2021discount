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
#
#     # the browser has been opened for twice?
#     # 頁面開了兩次 安捏乾丟？還是functional test我應該放在同一個def 不拆開寫？
#     def test_from_home_page(self):
#         self.browser.get('http://127.0.0.1:8000/')
#         time.sleep(1)
#         header_text = self.browser.find_element_by_tag_name('h1').text
#         self.assertIn('milet desu', header_text)
#
#     def test_about_page_template(self):
#         response = self.client.get('/about')
#         time.sleep(1)
#         self.assertTemplateUsed(response, 'about.html')
#         self.assertEqual(response.status_code, 200)
#
#     def test_contact_page_template(self):
#         response = self.client.get('/contact')
#         self.assertTemplateUsed(response, 'contact.html')
#         self.assertEqual(response.status_code, 200)
#
#     def test_anonymous_user_log_in(self):
#         # self.browser.get('http://127.0.0.1:8000/account/login')
#         # name_inputbox = self.browser.find_element_by_xpath('//*[@id="id_username"]')
#         # name_inputbox.send_keys('YYLRPL')
#         # name_inputbox.send_keys(Keys.ENTER)
#         # time.sleep(1)
#         # password_inputbox = self.browser.find_element_by_id('//*[@id="id_password"]')
#         # password_inputbox.send_keys('qazokm123')
#         # password_inputbox.send_keys(Keys.ENTER)
#         # time.sleep(4)
#         pass
#
#     # if anonymous user can only see 10 items in work_discount page
#     def test_anonymous_user_in_work_discount_page(self):
#         request = self.factory.get('/work_discount')
#         request.user = AnonymousUser()
#         response = work_discount(request)
#         self.assertEqual(response.status_code, 200)
#
#     # # if user can see 10+ items & card, extra discount in work_discount page
#     def test_authentic_user_in_work_discount_page(self):
#         request = self.factory.get('/work_discount')
#         request.user = self.user
#         response = work_discount(request)
#         # self.assertIn(response.content.decode('Card'))
#         # self.assertIn(response.content.decode(), '<th>Card</th>')
#         # self.assertIn(response.content.decode(), '<th>Cash Back</th>')
#         self.assertIn('Card', response.content.decode())
#         self.assertIn('Cash Back', response.content.decode())
#         self.assertEqual(response.status_code, 200)
#
#     # user log out
#     def test_authentic_user_log_out(self):
#         pass

# 留言板留言內容
# def test_can_leave_a_message_and_retrieve_it_later(self):
#     # 某人聽說有個很酷的在線待辦事項應用，他去看了這個應用的首頁
#     self.browser.get('http://localhost:8000/')
#
#     # 他注意到網頁的標題和頭都包含“土度”這個詞
#     self.assertIn('To-Do', self.browser.title)
#     header_text = self.browser.find_element_by_tag_name('h1').text
#     self.assertIn('To-Do', header_text)
#
#     # 应用邀请她输入一个待办事项
#     inputbox = self.browser.find_element_by_id('id_new_item')
#     self.assertEqual(
#         inputbox.get_attribute('placeholder'),
#         'Enter a to-do item'
#     )
#
#     # 她在一个文本框中输入了“Buy peacock feathers”(购买孔雀羽毛)
#     # 伊迪丝的爱好是使用假蝇做鱼饵钓鱼
#     inputbox.send_keys('Buy peacock feathers')


# if __name__ == '__main__':
#     unittest.main(warnings='ignore')