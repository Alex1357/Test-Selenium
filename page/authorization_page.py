from locators.authorization_page_locator import AuthorizationPageLocator as Locators
from page.base_page import BasePage


class AuthorizationPage(BasePage):

    def fill_fields_and_submit(self, username, password):
        if username != '':
            self.element_is_visible(Locators.USER_NAME).send_keys(username)
        if password != '':
            self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.LOGIN_BUTTON).click()
        return self.driver.current_url
