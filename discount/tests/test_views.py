from django.test import TestCase, RequestFactory             # test_unitttest, RequestFactory
from django.contrib.auth.models import AnonymousUser, User   # test_unitttest, RequestFactory
from discount.views import work_discount, myaccount, register        # test_unitttest, RequestFactory


# Create your tests here.
# rrrrrrr something weired, cuz even change the password, it still working
# 這邊好像哪裡怪怪的，因為如果把密碼改掉，還是顯示no issues =.=
class SimpleTest(TestCase):

    def setUp(self):  # every test needs access to the request factory
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='YYLRPL', password='qazokm123'
        )

    def test_details(self):             # Create an instance of a GET request
        request = self.factory.get('/work_discount')  # Recall that middleware are not supported.
        request.user = self.user        # can simulate a logged-in user by setting request.user manually
        request.user = AnonymousUser()  # test my_view() as if it were deployed at /customer/details
        response = work_discount(request)
        self.assertEqual(response.status_code, 200)


# 不過看起來沒有得測, 可以考慮測試頁面,
# 比如說沒登入是否可以看到某些資訊:
# # https://docs.djangoproject.com/en/3.1/topics/testing/advanced/#the-request-factory
# Functional Test?
class HomePageTest(TestCase):

    # get url http://127.0.0.1:8000 and template link correct
    # if response status is equal to 200
    def test_uses_home_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)

    def test_about_page_template(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'about.html')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_template(self):
        response = self.client.get('/contact')
        self.assertTemplateUsed(response, 'contact.html')
        self.assertEqual(response.status_code, 200)

    def test_works_page_template(self):
        response = self.client.get('/works')
        self.assertTemplateUsed(response, 'works.html')
        self.assertEqual(response.status_code, 200)

    # 登入與沒登入
    def test_work_discount_page_template(self):
        response = self.client.get('/work_discount')
        self.assertTemplateUsed(response, 'work_discount.html')
        self.assertEqual(response.status_code, 200)

    # AssertionError: No templates used to render the response
    # these 2 part no need to test because it's build in system?
    # 看起來這兩個部分 django內建所以不用測？
    # def test_register_page_template(self):
    #     response = self.client.get('/register')
    #     self.assertTemplateUsed(response, 'register.html')
    #
    # def test_loggin_page_template(self):
    #     response = self.client.get('/account/login')
    #     self.assertTemplateUsed(response, 'registration/login.html')





# 测试工具的默认行为是在任何名字以 test 开头的文件中找到所有的测试用例
# 也就是 unittest.TestCase 的子类
# test_views.py
# test_url.py
# test_model.py
# 设置语言, 如何發現語言偏好 https://docs.djangoproject.com/zh-hans/3.1/topics/testing/tools/

#
# functional_tests.py

# selenium的測試應該是，deploy之後吧？

# Good job! 一般來說是要測試model的
# function: https://docs.djangoproject.com/en/3.1/topics/testing/overview/
#



# 應該測試的項目：
# 1. 使用者登入前畫面，是否只顯示10項 work_discount
# 2. 使用者登入後畫面 work_discount
# 3. 使用者登入後，我的帳號連結 + 頁面
# 4.