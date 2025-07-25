import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from locators import Locators


class TestBurgerConstructor:

    @pytest.mark.parametrize("first_tab, second_tab, expected_name", [
        (Locators.SAUCES_SECTION, Locators.BUNS_SECTION, "Булки"),
        (Locators.BUNS_SECTION, Locators.SAUCES_SECTION, "Соусы"),
        (Locators.BUNS_SECTION, Locators.FILLINGS_SECTION, "Начинки")
    ])

    def test_burger_constructor_choosing_tabs(self, driver, first_tab, second_tab, expected_name):
        driver.get(MAIN_PAGE)

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(first_tab)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(second_tab)).click()

        assert WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ACTIVE_TAB)).text == expected_name
