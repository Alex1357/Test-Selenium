import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    service_driver = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_driver)
    driver.maximize_window()
    yield driver
    driver.quit()
