from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
from curl import *


class TestProfilePage:

    def test_go_to_profile_page(self, login):
        WebDriverWait(login, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

        assert login.current_url == PROFILE_PAGE

    def test_go_from_profile_page_to_constructor(self, login):
        WebDriverWait(login, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON)).click()

        assert login.current_url == MAIN_PAGE

    def test_go_from_profile_page_to_main_click_logo(self, login):
        WebDriverWait(login, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.LOGO_BUTTON)).click()

        assert login.current_url == MAIN_PAGE

    def test_logout_from_profile_page(self, login):
        WebDriverWait(login, 3).until(EC.element_to_be_clickable(Locators.PROFILE_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
        WebDriverWait(login, 3).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

        assert login.current_url == AUTH_PAGE
