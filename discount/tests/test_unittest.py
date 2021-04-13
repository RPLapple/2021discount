from django.test import TestCase


class HtmlPageTest(TestCase):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_all_works_page(self):
        response = self.client.get('/works')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'works.html')

    def test_work_discount_page(self):
        response = self.client.get('/work_discount')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'work_discount.html')

    def test_about_me_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_contact_page(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_login_page(self):
        response = self.client.get('/registration/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_register_page(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')


class LoginActionTest(TestCase):
    def test_login_action_username_password_null(self):
        test_data = {'username': '', 'password': ''}
        response = self.client.post('/registration/login/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This field is required", response.content)

    def test_login_action_username_password_error(self):
        test_data = {'username': 'YYL', 'password': ''}
        response = self.client.post('/registration/login/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This field is required", response.content)

    def test_login_action_success(self):
        test_data = {'username': 'YYL', 'password': 'qazokm123'}
        response = self.client.post('/registration/login/', data=test_data)
        self.assertEqual(response.status_code, 200)


class RegisterTest(TestCase):
    def test_register_action_username_password_null(self):
        test_data = {'username': '', 'password': ''}
        response = self.client.post('/accounts/register/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This field is required", response.content)

    def test_register_action_username_password_error(self):
        test_data = {'username': 'QQQ', 'password': 'qazokm', 'password2': 'qazokm'}
        response = self.client.post('/accounts/register/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"This password is too short", response.content)

    def test_register_action_success(self):
        pass


# class AdminPageTest(TestCase):
#     def test_products_filter_no_item(self):
#         pass
#
#     def test_products_filter_with_item_name(self):
#         pass
#
#     def test_products_filter_with_supermarket_name(self):
#         pass