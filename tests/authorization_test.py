from page.authorization_page import AuthorizationPage
from generator.generator import generator_user


class TestAuthorizationClass:
    AUTHORIZATION_URL = "https://www.saucedemo.com/"

    def test_standard_user(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('standard_user', 'secret_sauce')
        assert received_url != self.AUTHORIZATION_URL

    def test_locked_out_user(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('locked_out_user', 'secret_sauce')
        assert received_url != self.AUTHORIZATION_URL

    def test_problem_user(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('problem_user', 'secret_sauce')
        assert received_url != self.AUTHORIZATION_URL

    def test_performance_glitch_user(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('performance_glitch_user', 'secret_sauce')
        assert received_url != self.AUTHORIZATION_URL

    def test_generator_user(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        person = generator_user()
        print(person.email, person.password)
        received_url = authorization_page.fill_fields_and_submit(person.email, person.password)
        assert received_url == self.AUTHORIZATION_URL

    def test_user_without_password(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('standard_user', '')
        assert received_url == self.AUTHORIZATION_URL

    def test_user_without_username(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('', 'secret_sauce')
        assert received_url == self.AUTHORIZATION_URL

    def test_user_without_username_and_password(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('', '')
        assert received_url == self.AUTHORIZATION_URL
