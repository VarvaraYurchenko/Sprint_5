from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helper import *
from locators import Locators
from curl import *


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(REG_PAGE)
        name, email, password = generate_valid_registration_data()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert driver.current_url == AUTH_PAGE


    def test_registration_with_invalid_password_error(self, driver):
        driver.get(REG_PAGE)
        name, email, password = generate_registration_data_with_invalid_password()

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver,3).until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))

        assert driver.find_element(*Locators.PASSWORD_ERROR).text == "Некорректный пароль"
