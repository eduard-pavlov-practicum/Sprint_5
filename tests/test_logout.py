import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators


class TestLogout:

    def test_logout_successful(self, login_user):
        driver = login_user
        driver.find_element(
            *StartPageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located(StartPageLocators.LOGOUT_BUTTON))

        assert driver.find_element(
            *StartPageLocators.ENTER_AND_REGISTER_BUTTON).is_displayed
