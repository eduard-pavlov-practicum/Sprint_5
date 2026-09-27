import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, AdvertisementFormLocators, ProfilePageLocators


class TestPushAdvertisement:

    def test_push_advertisement_authorized_user_adverisement_visible(self, login_user, new_advert_name, new_advert_description, new_advert_price):
        driver = login_user
        driver.find_element(StartPageLocators.PUSH_AD_BUTTON['by'],
                            StartPageLocators.PUSH_AD_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((AdvertisementFormLocators.NAME_INPUT['by'],
                                                               AdvertisementFormLocators.NAME_INPUT['locator'])))
        driver.find_element(
            AdvertisementFormLocators.NAME_INPUT['by'], AdvertisementFormLocators.NAME_INPUT['locator']).send_keys(new_advert_name)
        driver.find_element(
            AdvertisementFormLocators.DESCRIPTION_TEXTAREA['by'], AdvertisementFormLocators.DESCRIPTION_TEXTAREA['locator']).send_keys(new_advert_description)
        driver.find_element(
            AdvertisementFormLocators.PRICE_INPUT['by'], AdvertisementFormLocators.PRICE_INPUT['locator']).send_keys(new_advert_price)
        unselected_button = driver.find_element(
            AdvertisementFormLocators.CONDITION_RADIO_UNSLECTED['by'], AdvertisementFormLocators.CONDITION_RADIO_UNSLECTED['locator'])
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(unselected_button))
        unselected_button.click()
        driver.find_element(
            AdvertisementFormLocators.CATEGORY_DROPDOWN_BUTTON['by'], AdvertisementFormLocators.CATEGORY_DROPDOWN_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((AdvertisementFormLocators.CATEGORY_DROPDOWN_MENU['by'],
                                                               AdvertisementFormLocators.CATEGORY_DROPDOWN_MENU['locator'])))
        category_buttons = driver.find_elements(AdvertisementFormLocators.CATEGORY_DROPDOWN_MENU['by'],
                                                AdvertisementFormLocators.CATEGORY_DROPDOWN_MENU['locator'])
        category_buttons[2].click()
        driver.find_element(
            AdvertisementFormLocators.CITY_DROPDOWN_BUTTON['by'], AdvertisementFormLocators.CITY_DROPDOWN_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((AdvertisementFormLocators.CITY_DROPDOWN_MENU['by'],
                                                               AdvertisementFormLocators.CITY_DROPDOWN_MENU['locator'])))
        city_buttons = driver.find_elements(AdvertisementFormLocators.CITY_DROPDOWN_MENU['by'],
                                            AdvertisementFormLocators.CITY_DROPDOWN_MENU['locator'])
        city_buttons[1].click()
        driver.find_element(
            AdvertisementFormLocators.PUBLISH_BUTTON['by'], AdvertisementFormLocators.PUBLISH_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.invisibility_of_element_located((AdvertisementFormLocators.PUBLISH_BUTTON['by'], AdvertisementFormLocators.PUBLISH_BUTTON['locator'])))
        avatar = WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((StartPageLocators.AVATAR['by'], StartPageLocators.AVATAR['locator'])))
        avatar.click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (ProfilePageLocators.MY_ADS_HEADING['by'], ProfilePageLocators.MY_ADS_HEADING['locator'])))
        assert driver.find_element(
            ProfilePageLocators.TARGET_ADVERTISEMENT['by'], ProfilePageLocators.TARGET_ADVERTISEMENT['locator']).text == new_advert_name

    def test_push_advertisement_not_authorized_user_modal_view_visible(self, driver):

        driver.find_element(
            StartPageLocators.PUSH_AD_BUTTON['by'], StartPageLocators.PUSH_AD_BUTTON['locator']).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StartPageLocators.MODAL_VIEW['by'],
                                                               StartPageLocators.MODAL_VIEW['locator'])))

        assert driver.find_element(StartPageLocators.MODAL_VIEW['by'],
                                   StartPageLocators.MODAL_VIEW['locator']).is_displayed
