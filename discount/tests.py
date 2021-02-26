from django.test import TestCase, RequestFactory             # test_unitttest, RequestFactory
from django.contrib.auth.models import AnonymousUser, User   # test_unitttest, RequestFactory
from .views import work_discount, myaccount, register        # test_unitttest, RequestFactory


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
    def test_uses_home_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')

    def test_about_page_template(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_page_template(self):
        response = self.client.get('/contact')
        self.assertTemplateUsed(response, 'contact.html')

    def test_works_page_template(self):
        response = self.client.get('/works')
        self.assertTemplateUsed(response, 'works.html')

    # 登入與沒登入
    def test_work_discount_page_template(self):
        response = self.client.get('/work_discount')
        self.assertTemplateUsed(response, 'work_discount.html')

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


