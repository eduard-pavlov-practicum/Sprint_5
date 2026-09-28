import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, AdvertisementFormLocators, ProfilePageLocators


class TestPushAdvertisement:

    def test_push_advertisement_authorized_user_adverisement_visible(self, login_user, new_advert_name, new_advert_description, new_advert_price):
        driver = login_user
        driver.find_element(*StartPageLocators.PUSH_AD_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AdvertisementFormLocators.NAME_INPUT))
        driver.find_element(
            *AdvertisementFormLocators.NAME_INPUT).send_keys(new_advert_name)
        driver.find_element(
            *AdvertisementFormLocators.DESCRIPTION_TEXTAREA).send_keys(new_advert_description)
        driver.find_element(
            *AdvertisementFormLocators.PRICE_INPUT).send_keys(new_advert_price)
        unselected_button = driver.find_element(
            *AdvertisementFormLocators.CONDITION_RADIO_UNSLECTED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(unselected_button))
        unselected_button.click()
        driver.find_element(
            *AdvertisementFormLocators.CATEGORY_DROPDOWN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AdvertisementFormLocators.CATEGORY_DROPDOWN_MENU))
        category_buttons = driver.find_elements(
            *AdvertisementFormLocators.CATEGORY_DROPDOWN_MENU)
        category_buttons[2].click()
        driver.find_element(
            *AdvertisementFormLocators.CITY_DROPDOWN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(AdvertisementFormLocators.CITY_DROPDOWN_MENU))
        city_buttons = driver.find_elements(
            *AdvertisementFormLocators.CITY_DROPDOWN_MENU)
        city_buttons[1].click()
        driver.find_element(
            *AdvertisementFormLocators.PUBLISH_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located(AdvertisementFormLocators.PUBLISH_BUTTON))
        avatar = WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(StartPageLocators.AVATAR))
        avatar.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            ProfilePageLocators.MY_ADS_HEADING))
        assert driver.find_element(
            *ProfilePageLocators.TARGET_ADVERTISEMENT).text == new_advert_name

    def test_push_advertisement_not_authorized_user_modal_view_visible(self, driver):

        driver.find_element(
            *StartPageLocators.PUSH_AD_BUTTON).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                StartPageLocators.MODAL_VIEW)
        ).is_displayed()
