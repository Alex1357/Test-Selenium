from selenium.webdriver.common.by import By


class AuthorizationPageLocator:
    USER_NAME = (By.CSS_SELECTOR, '#user-name')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')




