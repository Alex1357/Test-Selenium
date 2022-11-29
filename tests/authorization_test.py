from page.authorization_page import AuthorizationPage


class TestAuthorizationClass:
    AUTHORIZATION_URL = "https://www.saucedemo.com/"
    R_USERNAME = 'best_guy'
    R_PASSWORD = 'sunshine'

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

    def test_with_wrong_user(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit(self.R_USERNAME, self.R_PASSWORD)
        assert received_url == self.AUTHORIZATION_URL

    def test_user_without_username_and_password(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('', '')
        assert received_url == self.AUTHORIZATION_URL

    def test_user_without_password(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('standard_user', '')
        assert received_url == self.AUTHORIZATION_URL

    def test_user_with_wrong_password(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('standard_user', self.R_PASSWORD)
        assert received_url == self.AUTHORIZATION_URL

    def test_user_without_username(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit('', 'secret_sauce')
        assert received_url == self.AUTHORIZATION_URL

    def test_user_with_wrong_username(self, driver):
        authorization_page = AuthorizationPage(driver, self.AUTHORIZATION_URL)
        authorization_page.open()
        received_url = authorization_page.fill_fields_and_submit(self.R_USERNAME, 'secret_sauce')
        assert received_url == self.AUTHORIZATION_URL


